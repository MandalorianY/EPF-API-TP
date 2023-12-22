from fastapi import APIRouter
from src.schemas.message import MessageResponse
from src.services.analysis import predictions_classification_moodel

router = APIRouter()


@router.get("/predict", response_model=MessageResponse)
async def prediction_route():
    return MessageResponse(message=predictions_classification_moodel('src/data/Iris.csv'))
