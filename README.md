# AI Support Ticket Analyst

An AI-powered support ticket analysis system that allows users to ask natural-language questions about support tickets.

The system uses a local LLM through Ollama to understand user questions and converts them into structured queries. Pandas then performs the actual data analysis.

## Features

- CSV support ticket data ingestion
- Natural-language question answering
- Local LLM integration using Ollama
- Support ticket filtering and analysis
- Average response and resolution time analysis
- Agent performance analysis
- Customer rating analysis
- Anomaly detection using IQR
- Detection of unresolved high-priority tickets older than 24 hours
- REST API using FastAPI
- Interactive UI using Streamlit

## Project Architecture

text
User
  |
  v
Streamlit UI
  |
  v
FastAPI
  |
  v
Ollama LLM
  |
  v
Structured Query
  |
  v
Query Engine
  |
  v
Pandas DataFrame
  |
  +------> Anomaly Detector
  |
  v
API Response

##Project Structure

AI_Engineer_Assessment/
│
├── data/
│   └── support_tickets.csv
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── data_loader.py
│   ├── query_engine.py
│   ├── llm.py
│   ├── anomaly_detector.py
│   └── models.py
│
├── ui/
│   └── streamlit_app.py
│
├── tests/
│   └── test_api.py
│
├── requirements.txt
├── README.md
└── .gitignore

Technologies Used
Python
Pandas
FastAPI
Uvicorn
Streamlit
Ollama
Llama 3.2 3B
Pydantic

Installation

Create and activate a virtual environment:
python -m venv venv

Activate it:
.\venv\Scripts\Activate.ps1

Install dependencies:
pip install -r requirements.txt

Ollama Setup

Install Ollama and download the model:
ollama pull llama3.2:3b

Run the API

Start FastAPI:
uvicorn app.main:app --reload

API documentation:
http://127.0.0.1:8000/docs

Run the UI

Open another terminal, activate the virtual environment, and run:
streamlit run ui/streamlit_app.py

API Endpoints
Health Check

GET /health

Example response:

{
  "status": "ok"
}

Natural Language Query
POST /query

Example request:

{
  "question": "How many open tickets are there?"
}

Example response:

{
  "question": "How many open tickets are there?",
  "answer": 111
}

Anomaly Detection
GET /anomalies

##Example Questions

The system can answer questions such as:
How many open tickets are there?

How many critical tickets are there?

What is the average response time?

What is the average resolution time?

Which agent resolved the most tickets?

Which agent resolved the most tickets this month?

What is the average customer rating for Technical tickets?

Show me anomalies from this week.

Show me unresolved high-priority tickets older than 24 hours.

Show me all Critical tickets not resolved within 12 hours.


Cost

The project uses a local Ollama model, so no paid API key is required.

Limitations
The support ticket dataset is static.
"This week" and "this month" are interpreted relative to the latest date available in the dataset.
The system currently supports predefined query types.
Ollama must be installed locally to use the LLM functionality.