from fastapi import APIRouter
from src.schemas.message import MessageResponse
from src.services.data import load_dataset
router = APIRouter()


@router.get("/load", response_model=MessageResponse)
async def load_dataset_route() -> MessageResponse:
    """Load the Iris dataset from a CSV file and convert it to JSON format.\n
    Returns the Message with the dataset or an error message.
    """
    return MessageResponse(message=load_dataset('src/data/Iris.csv'))
