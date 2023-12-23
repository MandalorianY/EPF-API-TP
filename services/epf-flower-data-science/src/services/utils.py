import json
from sklearn.model_selection import train_test_split
from src.services.cleaning import procesing_datast
import pandas as pd
from typing import Tuple
import os


def split_dataset(file_path: str, test_size=0.2) -> Tuple[str, str]:
    """Split the dataset into train and test datasets.

    Args:
        file_path (str): the path to the dataset.
        test_size (float, optional): The size of the test dataset 0.2 is 20%. Defaults to 0.2.

    Returns:
        tuple (str, str): A tuple with the train and test datasets in JSON format or an error message.
    """
    try:
        if not os.path.exists(file_path):
            return ("The dataset was not found", "")
        data = procesing_datast(file_path)
        data = pd.DataFrame(json.loads(data))
        train, test = train_test_split(
            data, test_size=test_size, random_state=42, stratify=data['Species'])
        return train.to_json(orient='records'), test.to_json(orient='records')
    except Exception as e:
        print(f"An error occurred: {e}")
        return ("An error occurred during the dataset split", "")
