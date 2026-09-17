@echo off

echo Starting AI Support Ticket Analyst...

start "FastAPI" cmd /k "venv\Scripts\activate && uvicorn app.main:app --reload"

timeout /t 3 /nobreak >nul

start "Streamlit" cmd /k "venv\Scripts\activate && streamlit run ui\streamlit_app.py"

echo.
echo FastAPI: http://127.0.0.1:8000/docs
echo Streamlit: http://localhost:8501
echo.
pause
