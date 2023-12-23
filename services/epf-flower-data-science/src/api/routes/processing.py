from fastapi import APIRouter
from src.schemas.message import MessageResponse
from src.services.cleaning import procesing_datast
router = APIRouter()


@router.get("/processing", response_model=MessageResponse)
async def processed_dataset_route() -> MessageResponse:
    """ Process The Iris Dataset by removing the Id and Iris- from the Species column.\n
    Returns the dataset as a JSON or an error message.
    """
    return MessageResponse(message=procesing_datast('src/data/Iris.csv'))
