from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

from app.llm import ask_llm
from app.query_engine import execute_query
from app.anomaly_detector import detect_anomalies


app = FastAPI(
    title="AI Support Ticket Analyst",
    description="AI-powered support ticket analysis API",
    version="1.0"
)


class QueryRequest(BaseModel):
    question: str


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/query")
def query(request: QueryRequest):

    try:
        llm_response = ask_llm(request.question)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"LLM error: {str(e)}"
        )

    try:
        query = json.loads(llm_response)

    except json.JSONDecodeError:
        raise HTTPException(
            status_code=500,
            detail="LLM returned an invalid response."
        )

    try:
        result = execute_query(query)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Query processing error: {str(e)}"
        )

    return {
        "question": request.question,
        "answer": result
    }


@app.get("/anomalies")
def anomalies():

    result = detect_anomalies()

    return {
        "count": len(result),
        "anomalies": result.to_dict(orient="records")
    }