from fastapi import HTTPException, routing, APIRouter, Query
from pathlib import Path

from utils.file_helper import FileHelper
from .service import get_product_by_id

router = APIRouter(prefix="/products", tags=["Products"])


from .model import (
    CreateProductBody,
    Product,
    PartialPartiaProductBductBody,
    ProductType,
)

data_file = Path("assets/products.json")
file_helper = FileHelper(data_file)


@router.get("/types", summary="Get list of product types")
async def get_product_type():
    return {"types": [type for type in ProductType]}


@router.get("/{id}", summary="Get a product by id")
async def get_product(id: int):
    product = await get_product_by_id(id)

    return {"product": product}


@router.patch("/{id}", summary="Update a product information")
async def update_product(id: int, body: PartialPartiaProductBductBody):
    file_helper.update_product_to_file(id, body.dict())

    return {"success": True}


@router.delete("/{id}", summary="Delete a product by id")
async def delete_product(id: int):
    file_helper.delete_product_to_file(id)

    return {"success": True}


@router.get("/", summary="Get list of products")
async def get_products(
    type: ProductType = Query(None),
    offset: int | None = Query(0),
    limit: int | None = Query(2),
):
    products = file_helper.read_products_file()

    if type:
        products = [product for product in products if product.get("type") == type]

    start_index = offset * limit
    end_index = start_index + limit
    data = products[start_index:end_index]

    return {"data": data, "total": len(products)}


@router.post("/", summary="Create a product")
async def create_product(body: CreateProductBody):
    file_helper.write_product_to_file(body.dict())

    return {"success": True}
