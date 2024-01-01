import pytest
from fastapi.testclient import TestClient


class TestLoadRoute:
    @pytest.fixture
    def client(self) -> TestClient:
        """
        Test client for integration tests
        """

        from main import get_application

        app = get_application()

        client = TestClient(app, base_url="http://testserver")

        return client

    def test_predict(self, client):
        # Setup some test data
        url = "/predict"

        # Call the function to be tested
        response = client.get(url)

        # Assert the output
        assert response.status_code == 200
        assert response.json() == {
            "message": "[\"setosa\", \"virginica\", \"versicolor\", \"versicolor\", \"setosa\", \"versicolor\", \"setosa\", \"setosa\", \"virginica\", \"versicolor\", \"virginica\", \"virginica\", \"virginica\", \"versicolor\", \"setosa\", \"setosa\", \"setosa\", \"versicolor\", \"versicolor\", \"virginica\", \"setosa\", \"virginica\", \"versicolor\", \"virginica\", \"virginica\", \"versicolor\", \"versicolor\", \"setosa\", \"virginica\", \"setosa\"]"
        }
