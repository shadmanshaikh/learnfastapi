from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import OperationalError
from fastapi.middleware.cors import CORSMiddleware

# Database Configuration
DATABASE_URL = "postgresql://postgres:snowden135@localhost:5432/testwork"  # Update with your PostgreSQL credentials

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# FastAPI App Instance
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Database Model
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)

# Create the Database Table
Base.metadata.create_all(bind=engine)

# Pydantic Schema
class ItemCreate(BaseModel):
    name: str
    description: str

class ItemResponse(ItemCreate):
    id: int

    class Config:
        orm_mode = True

# Dependency: Database Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST Endpoint to Create an Item
@app.post("/items/", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Health Check Endpoint for Database Connection
@app.get("/health/")
def health_check():
    try:
        # Try connecting to the database
        with engine.connect() as connection:
            connection.execute("SELECT 1")  # Simple query to check connection
        return {"status": "Database is connected"}
    except OperationalError as e:
        raise HTTPException(status_code=500, detail="Database connection failed") from e
