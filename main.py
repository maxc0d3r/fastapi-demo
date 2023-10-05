from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
  return {"message": "fastapi demo"}

@app.get("/ping")
async def ping():
  return {"message": "pong"}
