from fastapi.testclient import TestClient
import os, sys
import json
from fastapi.responses import JSONResponse

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from main import app

client = TestClient(app)

def test_get_batch_list():
    response = client.get("/batch-list")
    assert response.status_code==200
    assert type(response.json()) == list
