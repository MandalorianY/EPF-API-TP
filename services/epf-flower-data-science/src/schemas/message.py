from src.schemas.camelcase import CamelCase


class MessageResponse(CamelCase):
    """A class to represent the response message.

    Args:
        CamelCase (_type_): The base class for the response message.
    """
    message: str
