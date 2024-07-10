from fastapi import HTTPException, routing, APIRouter, Query
from pathlib import Path

from utils.file_helper import FileHelper

router = APIRouter(prefix="/products", tags=["Products"])


from dto.products import (
    CreateProductBody,
    Product,
    PartialPartiaProductBductBody,
    ProductType,
)

data_file = Path("assets/products.json")
file_helper = FileHelper(data_file)


@router.get("/{id}")
async def get_product(id: int):
    products = file_helper.read_products_file()
    product = next(filter(lambda obj: obj.get("id") == id, products))

    return {"product": product}


@router.patch("/{id}")
async def update_product(id: int, body: PartialPartiaProductBductBody):
    file_helper.update_product_to_file(id, body.dict())

    return {"success": True}


@router.delete("/{id}")
async def delete_product(id: int):
    file_helper.delete_product_to_file(id)

    return {"success": True}


@router.get("/")
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


@router.post("/")
async def create_product(body: CreateProductBody):
    file_helper.write_product_to_file(body.dict())

    return {"success": True}


@router.get("/types/{type_name}")
async def get_product_type(type_name: ProductType):
    return {"type": type_name}
