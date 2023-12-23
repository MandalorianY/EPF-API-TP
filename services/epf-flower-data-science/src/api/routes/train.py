from fastapi import APIRouter
from src.schemas.message import MessageResponse
from src.services.analysis import training_classification_model

router = APIRouter()


@router.post("/train", response_model=MessageResponse)
async def train_route() -> MessageResponse:
    """Train the model with the given parameters and dataset and save it in the folder models folder.\n
    Returns a message with the training status or an error message.
    """
    return MessageResponse(message=training_classification_model('src/data/Iris.csv'))
