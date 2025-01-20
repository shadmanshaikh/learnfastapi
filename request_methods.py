from fastapi import FastAPI , Form , HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Employee(BaseModel):
    empid : str
    name : str
    designation : str
    salary : int

# GET request
@app.get('/api/v1/contact-us')
async def contactUs():
    contact_us = { "email" : "homecoming@gmail.com" , "address" : "deira" , "phone" : "055987321"}
    return contact_us

# POST request / collecting data from form
@app.post('/api/v1/add-emp')
async def addEmp(
    name: str = Form(...),
    empid: str = Form(...),
    designation: str = Form(...),
    salary: int = Form(...)
):
    employee = Employee(name=name, empid=empid, designation=designation, salary=salary)
    return employee

# PUT request
class compModel(BaseModel):
    name : str
    address : str

companies = {
    0 : {"name" : "sincron" , "address" : "dmcc"},
    1 : {"name" : "drape" , "address" : "jlt"},
}

@app.put('/api/v1/update_comp/{comp_id}' , response_model=compModel)
async def updateComp(comp_id : int , comp : compModel):
    if comp_id not in companies:
        raise HTTPException(status_code=404 , detail="ID not found")
    companies[comp_id] =  comp.dict()
    return companies[comp_id]

# DELETE request 
@app.delete('/api/v1/delete/{comp_id}')
async def delComp(comp_id : int):
    if comp_id not in companies:
        raise HTTPException(status_code=404 , detail="ID not found")
    del companies[comp_id]
    return {"message" : "Deleted the Company Details successfully"} , companies

