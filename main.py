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

app.include_router(productRoutes, prefix="/products", tags=["Products"])
####CRUD APIS -Products - JSON File
##http://localhost:8000/products/
##http://localhost:8000/products/create