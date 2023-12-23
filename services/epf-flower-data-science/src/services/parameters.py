import json
import os


def get_parameters(file_config_path: str) -> str:
    """Get the parameters from a JSON file and return them as a JSON string.

    Args:
        file_config_path (str): Path to the JSON file with the parameters.

    Returns:
        str: JSON string with the parameters or an error message.
    """
    try:
        if not os.path.exists(file_config_path):
            return ("The parameters file was not found")
        with open(file_config_path, 'r') as f:
            parameters = json.load(f)
        return json.dumps(parameters)
    except Exception as e:
        print(f"An error occurred: {e}")
        return ("An error occurred during the parameter loading")
