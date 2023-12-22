from fastapi import APIRouter
from src.schemas.message import MessageResponse
from src.services.data import download_data
router = APIRouter()


@router.post("/download_data")
def data() -> MessageResponse:
    download_data("src/data", "uciml/iris")
    return {"message": "Data downloaded successfully"}
