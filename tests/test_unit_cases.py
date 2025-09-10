
import pytest
from fastapi.testclient import TestClient
from api.main import app   # or your FastAPI entrypoint

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "Document Portal" in response.text

# def test_upload_file():
#     with open("tests/sample.pdf", "rb") as f:
#         response = client.post("/upload", files={"file": ("sample.pdf", f, "application/pdf")})
#     assert response.status_code == 200
#     assert response.json()["filename"] == "sample.pdf"