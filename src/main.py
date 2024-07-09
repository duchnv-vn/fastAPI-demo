from fastapi import HTTPException
from pathlib import Path

from core.app import (
    app,
    GET,
    POST,
    PATCH,
    DELETE
)
from utils.file_helper import FileHelper
from dto.products import (
    CreateProductBody,
    Product,
    PartialPartiaProductBductBody,
    ProductType
)

data_file = Path("assets/products.json")
file_helper = FileHelper(data_file)


@GET("/products/{id}")
async def get_product(id: int):
    products = file_helper.read_products_file()
    product = next(filter(lambda obj: obj.get("id") == id, products))

    return {"product": product}


@PATCH("/products/{id}")
async def update_product(id: int, body: PartialPartiaProductBductBody):
    file_helper.update_product_to_file(id, body.dict())

    return {"success": True}


@DELETE("/products/{id}")
async def delete_product(id: int):
    file_helper.delete_product_to_file(id)

    return {"success": True}


@GET("/products")
async def get_products(
    type: ProductType = None,
    offset: int = 0,
    limit: int = 2
):
    products = file_helper.read_products_file()

    if type:
        products = [
            product for product in products if product.get("type") == type]

    start_index = offset * limit
    end_index = start_index + limit
    data = products[start_index:end_index]

    return {"data": data, "total": len(products)}


@POST("/products")
async def create_product(body: CreateProductBody):
    file_helper.write_product_to_file(body.dict())

    return {"success": True}


@GET("/products/types/{type_name}")
async def get_product_type(type_name: ProductType):
    return {"type": type_name}


@GET("/files/{file_path:path}")
async def get_file(file_path: str):
    file_location = Path("assets") / file_path

    if not file_location.exists() or not file_location.is_file():
        raise HTTPException(status_code=404, detail="FILE_NOT_FOUND")

    with open(file_location, "r") as file:
        content = file.read()

    return content
