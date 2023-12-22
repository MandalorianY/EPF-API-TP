from fastapi import APIRouter
from src.schemas.message import MessageResponse
from src.services.analysis import training_classification_moodel

router = APIRouter()


@router.post("/train", response_model=MessageResponse)
async def train_route():
    training_classification_moodel('src/data/Iris.csv')
    return MessageResponse(message="Training Completed")
