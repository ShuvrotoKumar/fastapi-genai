from fastapi import APIRouter

productRoutes = APIRouter()

@productRoutes.get("/")
def getAllProducts():
    return {"message": "Get all products"}