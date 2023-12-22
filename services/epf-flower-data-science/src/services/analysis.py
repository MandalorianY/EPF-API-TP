from sklearn.neighbors import KNeighborsClassifier
from src.services.utils import split_dataset
from src.services.parameters import get_parameters
import pandas as pd
import joblib
import json


def training_classification_moodel(file_path: str) -> None:
    try:
        parameters = json.loads(get_parameters(
            'src/config/model_parameters.json'))
        train, _ = split_dataset(file_path)
        train = pd.DataFrame(json.loads(train))
        X_train = train.drop('Species', axis=1)
        y_train = train['Species']
        knn = KNeighborsClassifier(**parameters)
        knn.fit(X_train, y_train)
        joblib.dump(knn, 'src/data/models/knn.joblib')
    except Exception as e:
        print(f"An error occurred: {e}")

#  Add endpoint to make predictions with trained model and parameters.
# This endpoint have to send back the predictions as json.
# using src/data/models/knn.joblib


def predictions_classification_moodel(file_path: str) -> None:
    try:
        _, test = split_dataset(file_path)
        knn = joblib.load('src/data/models/knn.joblib')
        test = pd.DataFrame(json.loads(test))
        X_test = test.drop('Species', axis=1)
        predictions = knn.predict(X_test)
        return json.dumps(predictions.tolist())
    except Exception as e:
        print(f"An error occurred: {e}")
