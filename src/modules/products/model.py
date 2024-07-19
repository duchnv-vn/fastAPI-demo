from enum import Enum
from pydantic import BaseModel, Field
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
    name: str = Field(min_length=1, max_length=10, pattern=r"^[a-zA-Z0-9]+$")
    price: float
    type: ProductType


class PartialPartiaProductBductBody(BaseModel):
    name: str | None = Field(min_length=1, max_length=10, pattern=r"^[a-zA-Z0-9]+$")
    price: float | None = None
    type: ProductType | None = None
