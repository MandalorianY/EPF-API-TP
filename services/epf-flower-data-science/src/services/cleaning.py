from src.services.data import load_dataset
import pandas as pd
import json


def procesing_datast(file_path: str) -> str:
    json_data = load_dataset(file_path)
    data = json.loads(json_data)
    data = pd.DataFrame(data)
    data.drop('Id', axis=1, inplace=True)
    data["Species"] = data['Species'].str.replace('Iris-', '')
    return data.to_json(orient='records')
