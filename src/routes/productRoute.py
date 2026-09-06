from fastapi import APIRouter
from src.utils.utils import get_all_products
productRoutes = APIRouter()

@productRoutes.get("/")
def getAllProducts():
    return get_all_products() 

@productRoutes.get("/{id}")
def getOneProduct(id: int):
    print("ID:", id)
    allProducts = get_all_products()
    for product in allProducts:
        if product["id"] == id:
            return product
    return {"message": "Product not found"}
@productRoutes.post("/create")
def createNewProduct():
    return {"message": "Create new product"}

