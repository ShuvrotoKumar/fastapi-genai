from fastapi import APIRouter
from src.utils.utils import get_all_products
productRoutes = APIRouter()

@productRoutes.get("/")
def getAllProducts():
    return get_all_products() 



@productRoutes.post("/create")
def createNewProduct():
    return {"message": "Create new product"}

