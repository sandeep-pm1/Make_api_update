from fastapi.testclient import TestClient
from fastapi.responses import FileResponse
import os, sys, json

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from main import app

client = TestClient(app)

def test_get_legend():
    response = client.get("/legend")
    if response.status_code==200:
        assert type(response.json()) == dict

def test_read_inexistence_item():
    response = client.get("/legend")
    if response.status_code==404:
        assert response.json() == {"detail": "Data not Available"}