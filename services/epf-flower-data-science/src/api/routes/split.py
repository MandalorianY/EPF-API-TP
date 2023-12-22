from fastapi import APIRouter
from src.schemas.message import MessageResponse
from src.services.utils import split_dataset
import json
router = APIRouter()


@router.get("/split", response_model=MessageResponse)
async def split_dataset_route():
    test, train = split_dataset('src/data/Iris.csv')
    combined_data = {
        'train': json.loads(train),
        'test': json.loads(test)
    }
    print(json.dumps(combined_data))
    return MessageResponse(message=json.dumps(combined_data))
