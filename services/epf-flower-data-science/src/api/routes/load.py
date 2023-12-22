from fastapi import APIRouter
from src.schemas.message import MessageResponse
from src.services.data import load_dataset
router = APIRouter()


@router.get("/load", response_model=MessageResponse)
async def load_dataset_route():
    return MessageResponse(message=load_dataset('src/data/Iris.csv'))
