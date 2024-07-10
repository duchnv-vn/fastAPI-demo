from fastapi import HTTPException, routing, APIRouter
from pathlib import Path

router = APIRouter(prefix="/files", tags=["Files"])


@router.get("/{file_path:path}")
async def get_file(file_path: str):
    file_location = Path("assets") / file_path

    if not file_location.exists() or not file_location.is_file():
        raise HTTPException(status_code=404, detail="FILE_NOT_FOUND")

    with open(file_location, "r") as file:
        content = file.read()

    return content
