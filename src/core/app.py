from fastapi import FastAPI

from modules.files.routes import router as files_router
from modules.products.routes import router as products_router

app = FastAPI()

app.include_router(files_router)
app.include_router(products_router)
