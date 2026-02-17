from fastapi import FastAPI
from app.workflows import run_workflow
import asyncio

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Durable Execution Engine Running"}

@app.post("/run")
async def start():
    await run_workflow()
    return {"status": "workflow executed"}
