from fastapi import APIRouter
from src.schemas.message import MessageResponse
from src.services.utils import split_dataset
import json
router = APIRouter()


@router.get("/split", response_model=MessageResponse)
async def split_dataset_route() -> MessageResponse:
    """Split the dataset into train and test sets and return them as JSON.\n
    Returns a JSON with the train and test sets or an error message.
    """
    test, train = split_dataset('src/data/Iris.csv')
    message_str = ""
    if train != "":
        combined_data = {
            'train': json.loads(train),
            'test': json.loads(test)
        }
        message_str = json.dumps(combined_data)
    else:
        message_str = test
    return MessageResponse(message=message_str)
