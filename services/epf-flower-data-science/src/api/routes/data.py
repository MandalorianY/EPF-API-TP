from fastapi import APIRouter
from src.schemas.message import MessageResponse
from src.services.data import download_data
router = APIRouter()


@router.post("/download_data")
def data() -> MessageResponse:
    """  Download the Iris dataset from UCI Machine Learning Repository and unzip it into the data folder\n
    return the message with the result of the operation.
    """

    return_code = download_data("src/data", "uciml/iris")
    message = "Download is successful" if return_code else "Error downloading the dataset"
    return MessageResponse(message=message)
