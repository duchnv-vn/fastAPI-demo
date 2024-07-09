from enum import Enum
from pydantic import BaseModel
from typing import Union


class ProductType(str, Enum):
    laptop = "laptop"
    computer = "computer"
    smartphone = "smartphone"
    tablet = "tablet"


class Product(BaseModel):
    id: int
    name: str
    price: float
    type: ProductType


class CreateProductBody(BaseModel):
    name: str
    price: float
    type: ProductType


class PartialPartiaProductBductBody(BaseModel):
    name: Union[str, None] = None
    price: Union[float, None] = None
    type: Union[ProductType, None] = None
