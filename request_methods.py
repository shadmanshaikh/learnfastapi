from fastapi import FastAPI , Form
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
companies = {
    0 : {"name" : "sincron" , "address" : "dmcc"},
    1 : {"name" : "drape" , "address" : "jlt"},
}


