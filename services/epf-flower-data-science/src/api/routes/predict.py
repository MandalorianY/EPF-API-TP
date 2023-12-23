from fastapi import APIRouter
from src.schemas.message import MessageResponse
from src.services.analysis import predictions_classification_moodel

router = APIRouter()


@router.get("/predict", response_model=MessageResponse)
async def prediction_route() -> MessageResponse:
    """Predict the class of the flower in the test dataset based on the model.\n
    Returns the JSON with the prediction or an error message.
    """
    return MessageResponse(message=predictions_classification_moodel('src/data/Iris.csv'))
