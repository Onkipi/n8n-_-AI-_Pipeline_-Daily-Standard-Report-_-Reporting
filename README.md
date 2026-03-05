
# n8n AI Pipelines

Production-ready n8n workflow templates for enterprise AI automation.

## Included Workflows
- Weekly AI Project Status Reporter
- Document Intelligence Pipeline
- AI Email Triage Agent

## Setup

Install n8n (Docker recommended):

docker run -it --rm --name n8n -p 5678:5678 n8nio/n8n

Open UI: http://localhost:5678

## Import Workflows
1. Go to Workflows → Import
2. Upload JSON from /workflows

## Optional: Deploy via API

pip install -r requirements.txt
cp .env.example .env

python scripts/deploy_workflows.py
