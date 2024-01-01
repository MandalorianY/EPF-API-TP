from fastapi import APIRouter
from src.schemas.message import MessageResponse
from src.services.parameters import get_parameters_from_firebase
router = APIRouter()


@router.get("/get_params_firebase", response_model=MessageResponse)
async def prediction_route():
    """Get the parameters of the model.\n
    Returns a JSON with the parameters or an error message.
    """
    return MessageResponse(message=get_parameters_from_firebase('parameters', 'model_parameters'))
