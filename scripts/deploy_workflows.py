
import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

N8N_URL = os.getenv("N8N_URL", "http://localhost:5678")
API_KEY = os.getenv("N8N_API_KEY")

HEADERS = {
    "X-N8N-API-KEY": API_KEY,
    "Content-Type": "application/json"
}

WORKFLOW_DIR = "../workflows"

def deploy_workflow(file):
    with open(file) as f:
        data = json.load(f)
    r = requests.post(f"{N8N_URL}/api/v1/workflows", headers=HEADERS, json=data)
    print(file, r.status_code, r.text)

if __name__ == "__main__":
    for wf in os.listdir(WORKFLOW_DIR):
        deploy_workflow(os.path.join(WORKFLOW_DIR, wf))
