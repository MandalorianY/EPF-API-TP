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

    def test_params(self, client):
        # Setup some test data
        url = "/get_params"

        # Call the function to be tested
        response = client.get(url)

        # Assert the output
        assert response.status_code == 200
        assert response.json() == {
            "message": "{\"n_neighbors\": 5, \"weights\": \"uniform\", \"algorithm\": \"auto\"}"
        }

    def test_params_firebase(self, client):
        # Setup some test data
        url = "/get_params_firebase"

        # Call the function to be tested
        response = client.get(url)

        # Assert the output
        assert response.status_code == 200
        assert response.json() == {
            "message": "{\"n_neighbors\": 5, \"weights\": \"uniform\", \"algorithm\": \"auto\"}"
        }
