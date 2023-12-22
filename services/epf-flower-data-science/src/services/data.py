from kaggle.api.kaggle_api_extended import KaggleApi
from requests.exceptions import HTTPError
import pandas as pd


def download_data(data_path: str, dataset_url: str) -> None:
    try:
        print(f"Downloading data from {dataset_url} to {data_path}")
        api = KaggleApi()
        api.authenticate()
        api.dataset_download_files(
            dataset=dataset_url, path=data_path, unzip=True)
    except HTTPError as e:
        print(f"An HTTP error occurred: {e.response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")


def load_dataset(file_path: str) -> str:
    try:
        data = pd.read_csv(file_path)
        return data.to_json(orient='records')
    except Exception as e:
        print(f"An error occurred: {e}")
