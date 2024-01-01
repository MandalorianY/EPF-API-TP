import json
from src.services.cleaning import procesing_datast
from unittest.mock import patch, MagicMock
import unittest
import pandas as pd

mock_dataset = [
    {
        "Id": 1,
        "SepalLengthCm": 5.1,
        "SepalWidthCm": 3.5,
        "PetalLengthCm": 1.4,
        "PetalWidthCm": 0.2,
        "Species": "Iris-setosa"
    },
    {
        "Id": 2,
        "SepalLengthCm": 4.9,
        "SepalWidthCm": 3.0,
        "PetalLengthCm": 1.4,
        "PetalWidthCm": 0.2,
        "Species": "Iris-setosa"
    },
    {
        "Id": 3,
        "SepalLengthCm": 4.7,
        "SepalWidthCm": 3.2,
        "PetalLengthCm": 1.3,
        "PetalWidthCm": 0.2,
        "Species": "Iris-setosa"
    }
]

expected = [
    {
        "SepalLengthCm": 5.1,
        "SepalWidthCm": 3.5,
        "PetalLengthCm": 1.4,
        "PetalWidthCm": 0.2,
        "Species": "setosa"
    },
    {
        "SepalLengthCm": 4.9,
        "SepalWidthCm": 3.0,
        "PetalLengthCm": 1.4,
        "PetalWidthCm": 0.2,
        "Species": "setosa"
    },
    {
        "SepalLengthCm": 4.7,
        "SepalWidthCm": 3.2,
        "PetalLengthCm": 1.3,
        "PetalWidthCm": 0.2,
        "Species": "setosa"
    }
]


class TestCleaning(unittest.TestCase):
    @patch('cleaning.os.path.exists')
    @patch('cleaning.load_dataset')
    @patch('cleaning.pd.DataFrame')
    def test_procesing_datast(self, mock_df_class, mock_load_dataset, mock_exists):
        # Arrange
        mock_exists.return_value = True
        mock_load_dataset.return_value = json.dumps(mock_dataset)
        mock_df = MagicMock(spec=pd.DataFrame)
        mock_df_class.return_value = mock_df
        mock_df.drop.return_value = mock_df
        mock_df.to_json.return_value = json.dumps(expected)
        file_path = 'dummy_path'

        # Act
        result = procesing_datast(file_path)

        # Assert
        self.assertEqual(result, json.dumps(expected))
        mock_exists.assert_called_once_with(file_path)
        mock_load_dataset.assert_called_once_with(file_path)
        mock_df_class.assert_called_once_with(
            json.loads(mock_load_dataset.return_value))
        mock_df.drop.assert_called_once_with('Id', axis=1, inplace=True)
        mock_df.to_json.assert_called_once_with(orient='records')


if __name__ == '__main__':
    unittest.main()
