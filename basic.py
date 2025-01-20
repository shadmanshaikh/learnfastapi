from fastapi import FastAPI
import uvicorn
app = FastAPI()


# hello route 
@app.get('/')
async def root():
    return {"hello:chadmax"}

# lets perfom crud

# creating a list
maxxer = ['chadmax', 'gigachad' , 'rizzler']

# read & update from a list
@app.get('/show-data')
async def showData():
    if "tyler" not in maxxer:
        maxxer.append("tyler")
    else:
        "Tyler already present"
    return maxxer

# delete from a list
@app.get('/delete')
async def deleData():
    if "gigachad" in maxxer:
        maxxer.remove("gigachad")
    return maxxer
    




