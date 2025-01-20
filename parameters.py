from fastapi import FastAPI , HTTPException
from typing import Optional

app = FastAPI()

# path parameters 
companies = {
    0 : {"name" : "sincron" , "address" : "dmcc"},
    1 : {"name" : "drape" , "address" : "jlt"},
}

@app.get('/get-comp/{comp_id}')
async def getComp(comp_id : int):
    if comp_id not in companies:
        raise HTTPException(status_code=404 , detail="ID not found")
    return companies[comp_id]

# query parameters
@app.get('/search')
async def searching(id : int , q: Optional[int] =  None):
    return companies[id]