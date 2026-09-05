from fastapi import FastAPI
from src.routes.productRoute import productRoutes
app = FastAPI(
    title="My FastAPI Course",
    description="A simple FastAPI course",
    version="0.1.0"
)

@app.get("/home")
def home():
    return {"message": "Welcome to my FastAPI course!"}


####CRUD APIS -Products - JSON File

app.add_routes("/", productRoutes)