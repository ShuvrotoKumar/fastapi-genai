from fastapi import FastAPI

app = FastAPI(
    title="My FastAPI Course",
    description="A simple FastAPI course",
    version="0.1.0"
)

@app.get("/")
def home():
    return {"message": "Welcome to my FastAPI course!"}


####CRUD APIS -Products - JSON File