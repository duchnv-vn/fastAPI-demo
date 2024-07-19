from fastapi import HTTPException

from pathlib import Path

from utils.file_helper import FileHelper

data_file = Path("assets/products.json")
file_helper = FileHelper(data_file)


async def get_product_by_id(id: int):
    products = file_helper.read_products_file()

    try:
        product = next(filter(lambda obj: obj.get("id") == id, products))
    except StopIteration as error:
        print("get_product_by_id error", error)
        raise HTTPException(status_code=404, detail="Product not found")
    except:
        raise HTTPException(status_code=500, detail="Something went wrong")

    return product
