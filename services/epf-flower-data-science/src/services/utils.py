import json
from sklearn.model_selection import train_test_split
from src.services.cleaning import procesing_datast
import pandas as pd


def split_dataset(file_path, test_size=0.2):
    # split the iris dataset as train and
    # test and send back a json with both
    data = procesing_datast(file_path)
    data = json.loads(data)
    data = pd.DataFrame(data)
    train, test = train_test_split(
        data, test_size=test_size, random_state=42, stratify=data['Species'])
    return train.to_json(orient='records'), test.to_json(orient='records')
