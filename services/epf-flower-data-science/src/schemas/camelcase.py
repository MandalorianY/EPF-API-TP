from fastapi_utils.camelcase import snake2camel
from pydantic import BaseConfig, BaseModel
from pydantic.generics import GenericModel


def snake_2_camel(m: str) -> str:
    """Convert snake_case to camelCase for Pydantic models

    Args:
        m (str): The string to convert.

    Returns:
        str: The converted string.
    """
    return snake2camel(m, True)


class CamelCase(BaseModel):
    class Config(BaseConfig):
        allow_population_by_field_name = True
        alias_generator = snake_2_camel


class GenericCamelCase(GenericModel):
    class Config(BaseConfig):
        allow_population_by_field_name = True
        alias_generator = snake_2_camel
