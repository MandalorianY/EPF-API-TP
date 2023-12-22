import json


def get_parameters(file_config_path) -> str:
    try:
        with open(file_config_path, 'r') as f:
            parameters = json.load(f)
        return json.dumps(parameters)
    except Exception as e:
        print(f"An error occurred: {e}")
