# AI Support Ticket Analyst

An AI-powered support ticket analysis system that allows users to ask natural-language questions about support tickets.

The system uses a local LLM through Ollama to convert user questions into structured queries. Pandas performs the actual data analysis.

## Features

- CSV data ingestion
- Natural-language querying
- Local LLM using Ollama
- Support ticket analysis and filtering
- Agent and customer rating analysis
- IQR-based anomaly detection
- FastAPI REST API
- Streamlit UI
- Automated API tests

## Architecture

```text
User
  ↓
Streamlit UI
  ↓
FastAPI
  ↓
Ollama LLM
  ↓
Structured Query
  ↓
Pandas Query Engine
  ↓
Result
```

## Project Structure

```text
AI_Engineer_Assessment/
├── app/
│   ├── main.py
│   ├── data_loader.py
│   ├── query_engine.py
│   ├── llm.py
│   ├── anomaly_detector.py
│   └── models.py
├── data/
│   └── support_tickets.csv
├── tests/
│   └── test_api.py
├── ui/
│   └── streamlit_app.py
├── requirements.txt
├── README.md
├── start.bat
└── .gitignore
```

## Technologies

- Python
- Pandas
- FastAPI
- Streamlit
- Ollama
- Llama 3.2 3B
- Pytest

## Setup

Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Install the Ollama model:

```powershell
ollama pull llama3.2:3b
```

## Run

Start the complete application:

```powershell
.\start.bat
```

FastAPI:

```text
http://127.0.0.1:8000/docs
```

Streamlit:

```text
http://localhost:8501
```

## API Endpoints

### Health

```text
GET /health
```

### Natural Language Query

```text
POST /query
```

Example:

```json
{
  "question": "How many open tickets are there?"
}
```

### Anomaly Detection

```text
GET /anomalies
```

## Example Questions

- How many open tickets are there?
- How many critical tickets are unresolved?
- What is the average response time?
- Which agent resolved the most tickets?
- Which agent has the lowest average customer rating?
- Show me anomalies from this week.
- Show me unresolved high-priority tickets older than 24 hours.

## LLM Approach

The LLM interprets the user's question and produces a structured query.

Example:

```json
{
  "action": "count",
  "column": "status",
  "value": "Open"
}
```

Pandas then performs the actual calculation. This keeps numerical results deterministic.

## Anomaly Detection

The system uses the IQR method:

```text
IQR = Q3 - Q1
Upper Limit = Q3 + 1.5 × IQR
```

Tickets above the upper limit are treated as resolution-time anomalies.

## Testing

Run:

```powershell
pytest -q
```

Current result:

```text
5 passed
```

## Cost

The project uses a local Ollama model and does not require a paid API key.

## Limitations

- Dataset is static.
- Only predefined query types are currently supported.
- Ollama must be installed locally.