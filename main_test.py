import pytest
from main import app
import re


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_xss_vulnerability(client):
    response = client.get('/xss?q=<script>alert("xss")</script>')
    assert response.status_code == 200
    # Check that the response does not contain any <script> tags
    dangerous_pattern = re.compile(r"<\s*script\s*>.*?<\s*/\s*script\s*>", re.IGNORECASE | re.DOTALL)
    assert not dangerous_pattern.search(
        response.get_data(as_text=True)), "Response contains a dangerous <script> pattern"


def test_functionality(client):
    response = client.get('/xss?q=alice')
    assert response.status_code == 200
    assert response.get_json()["results"] == [{"name": "Alice Johnson", "age": 30}]

