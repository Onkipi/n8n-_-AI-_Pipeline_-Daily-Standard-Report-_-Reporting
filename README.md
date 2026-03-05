# ⚙️ n8n AI Pipelines
### Ready-to-Import AI Workflow Templates for Enterprise Automation

> Built by **Vijay Kashyab** | AI Program Manager & Architect
> These templates are pulled directly from production enterprise automation workflows

---

## What's Inside

10 production-ready n8n workflow templates that connect AI capabilities to real business processes — no custom API code required.

---

## Workflow Templates

### 1️⃣ Weekly AI Project Status Reporter
**Trigger:** Every Monday 8 AM
**Flow:** Jira API → fetch all projects → Code Node (format data) → OpenAI (generate executive summary) → Gmail (send to stakeholders)
**Business Value:** Eliminates 3 hours/week of manual status reporting

```javascript
// n8n Code Node: Format project data for LLM
const projects = $input.all();
let summary = "Weekly AI Portfolio Status:\n\n";
for (const p of projects) {
  summary += `Project: ${p.json.name}\n`;
  summary += `Status: ${p.json.status} | Budget: ${p.json.budget_pct}% used\n`;
  summary += `Open Risks: ${p.json.open_risks} | Sprint: ${p.json.sprint}\n\n`;
}
return [{ json: { summary } }];
```

---

### 2️⃣ Document Intelligence Pipeline
**Trigger:** New file in Google Drive folder
**Flow:** Drive → Download → Text extraction → OpenAI (extract: dates, budget, risks, actions) → Code Node (parse JSON) → Jira (create tasks) → Slack (notify team)
**Business Value:** 40-minute manual document review → 6-minute automated extraction

---

### 3️⃣ AI Email Triage Agent
**Trigger:** New email in Gmail inbox
**Flow:** Gmail → OpenAI (classify: Urgent/Normal/FYI + category) → Route to folder OR auto-draft reply for routine queries → Slack alert for urgent items
**Business Value:** 46% reduction in email processing time

---

### 4️⃣ RAG Knowledge Base Updater
**Trigger:** Weekly schedule OR webhook from document management system
**Flow:** Fetch new/updated documents → Extract text → HTTP Request to embedding API → Upsert to vector store (pgvector/Pinecone)
**Business Value:** Keeps AI assistants current without manual re-indexing

---

### 5️⃣ AI Risk Monitor
**Trigger:** Daily 6 AM
**Flow:** Jira/Asana API → fetch all risks → OpenAI (assess if any risks escalated based on recent activity) → IF new High risks → Slack alert + email to sponsor
**Business Value:** Proactive risk detection vs. weekly manual review

---

### 6️⃣ LLM Cost Monitor & Alerter
**Trigger:** Every 6 hours
**Flow:** OpenAI Usage API → calculate spend vs. daily budget → IF >70% → Slack warning. IF >90% → PagerDuty alert + auto-throttle non-critical queries
**Business Value:** Prevents LLM cost overruns (common in enterprise AI programs)

---

### 7️⃣ Automated Model Performance Reporter
**Trigger:** Monthly (1st of month)
**Flow:** LangSmith API → pull RAGAS scores for all models → Code Node (generate trend analysis) → OpenAI (write executive AI health narrative) → Email to AI governance board
**Business Value:** Automated compliance reporting for GDPR/SOC2 AI governance

---

### 8️⃣ Meeting Notes → Action Items Pipeline
**Trigger:** Webhook from calendar (meeting ended)
**Flow:** Fetch recording transcript → OpenAI (extract: decisions, action items, owners, deadlines) → Create Jira tasks → Email summary to attendees
**Business Value:** Eliminates post-meeting admin; 85% faster action capture

---

### 9️⃣ AI-Powered Support Ticket Triage
**Trigger:** New Zendesk/Freshdesk ticket
**Flow:** Fetch ticket → OpenAI (classify tier: AI-resolvable/human-needed + urgency) → IF Tier 1: RAG system generates response draft → Agent reviews and sends. IF Tier 2/3: Route to appropriate team with AI-generated context summary
**Business Value:** 58% tickets resolved by AI without human intervention

---

### 🔟 Stakeholder Communication Automator
**Trigger:** Sprint completion webhook from Jira
**Flow:** Fetch sprint metrics (velocity, burndown, risks) → OpenAI (generate stakeholder-appropriate summary per audience: Executive, Technical, Business) → Send personalized emails per stakeholder type
**Business Value:** Right message to right audience, automatically

---

## Setup Guide

```bash
# Option 1: Docker (recommended for production)
docker run -it --rm --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  -e OPENAI_API_KEY=your_key_here \
  n8nio/n8n

# Option 2: npm global install
npm install n8n -g
n8n start

# Access UI at: http://localhost:5678
```

## Import a Workflow
1. Open n8n UI → Workflows → Import
2. Upload the `.json` file from `/workflows/` directory
3. Configure credentials (OpenAI, Gmail, Jira, Slack)
4. Activate the workflow

---

## Required Credentials Setup

| Credential | Used In | Setup |
|---|---|---|
| OpenAI API | All AI workflows | Settings → Credentials → OpenAI |
| Gmail OAuth2 | Email workflows | Google Cloud Console → OAuth2 |
| Jira API | PM workflows | Jira → Account Settings → API Token |
| Slack | Alert workflows | Slack → Apps → Incoming Webhooks |
| Pinecone/pgvector | RAG workflows | Vector DB API key |

---

`n8n` `OpenAI` `LangChain` `Python` `FastAPI` `PostgreSQL` `Pinecone` `Slack` `Jira` `Gmail`
