from sklearn.neighbors import KNeighborsClassifier
from src.services.utils import split_dataset
from src.services.parameters import get_parameters
import pandas as pd
import joblib
import json
import os


def training_classification_model(file_path: str) -> str:
    """
    Train a classification model based on KNN algorithm and parameters and save it in a joblib file.
    Args:
        file_path (str): Path to the dataset.
    Returns:
        str: Message with the result of the training or an error message.
    """
    try:
        parameters = json.loads(get_parameters(
            'src/config/model_parameters.json'))
        train, _ = split_dataset(file_path)
        train = pd.DataFrame(json.loads(train))
        X_train = train.drop('Species', axis=1)
        y_train = train['Species']
        knn = KNeighborsClassifier(**parameters)
        knn.fit(X_train, y_train)
        joblib.dump(knn, 'src/models/knn.joblib')
        return ("The model was trained and saved")
    except Exception as e:
        print(f"An error occurred: {e}")
        return ("An error occurred during the training")


def predictions_classification_moodel(file_path: str) -> str:
    """
    Predict the species of the flowers in the test dataset based on the trained model

    Args:
        file_path (str): _description_

    Returns:
        str: JSON string with the predictions or an error message.
    """
    try:
        if not os.path.exists(file_path):
            return ("The dataset was not found")
        if not os.path.exists('src/models/knn.joblib'):
            training_classification_model(file_path)
        _, test = split_dataset(file_path)
        knn = joblib.load('src/data/models/knn.joblib')
        test = pd.DataFrame(json.loads(test))
        X_test = test.drop('Species', axis=1)
        predictions = knn.predict(X_test)
        return json.dumps(predictions.tolist())
    except Exception as e:
        print(f"An error occurred: {e}")
        return ("An error occurred during the prediction")
