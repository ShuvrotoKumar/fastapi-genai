from fastapi import APIRouter,HTTPException
from src.utils.utils import get_all_products
productRoutes = APIRouter()
##get all products
# @productRoutes.get("/")
# def getAllProducts():
#     return get_all_products() 
##get one product by id path parameter
@productRoutes.get("/{id}")
def getOneProduct(id: int):
    allProducts = get_all_products()
    for product in allProducts:
        if product["id"] == id:
            return product
    return HTTPException(status_code=404, detail="Product not found")

##get one product by id query parameter
@productRoutes.get("/")
def getOneProductQuery(product_id:int = None):
    allProducts = get_all_products()

    if not product_id:
        return allProducts
    
    for product in allProducts:
        if product["id"] == product_id:
            return product
    return HTTPException(status_code=404, detail="Product not found")


##create new product
@productRoutes.post("/create")
def createNewProduct():
    return {"message": "Create new product"}

