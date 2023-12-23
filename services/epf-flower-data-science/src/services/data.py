from kaggle.api.kaggle_api_extended import KaggleApi
from requests.exceptions import HTTPError
import pandas as pd
import os


def download_data(data_path: str, dataset_url: str) -> bool:
    """
    Download the dataset from Kaggle and unzip it.

    Args:
        data_path (str): Data path to save the dataset.
        dataset_url (str): Dataset URL in Kaggle with name of the user/dataset.

    Returns:
        bool: True if download is successful, False if it fails.
    """
    try:
        print(f"Downloading data from {dataset_url} to {data_path}")
        api = KaggleApi()
        api.authenticate()
        api.dataset_download_files(
            dataset=dataset_url, path=data_path, unzip=True)
        return True
    except HTTPError as e:
        print(f"An HTTP error occurred: {e.response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return False


def load_dataset(file_path: str) -> str:
    """Load the dataset from a CSV file and convert it to JSON format.

    Args:
        file_path (str): Path to the dataset.

    Returns:
        str: JSON string with the dataset or an error message.
    """
    try:
        if not os.path.exists(file_path):
            return ("The dataset was not found")
        data = pd.read_csv(file_path)
        return data.to_json(orient='records')
    except Exception as e:
        print(f"An error occurred: {e}")
        return ("An error occurred")
