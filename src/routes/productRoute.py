from fastapi import APIRouter

productRoutes = APIRouter()


def getAllProducts():
    return {"message": "Get all products"}