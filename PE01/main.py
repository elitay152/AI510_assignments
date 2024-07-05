from fastapi import FastAPI

# create app instance
app = FastAPI()


@app.get("/") # decorator
async def root(): # async function
    return {"message": "Hello World"} # function output