# 🧪 Async Document Q&A Microservice

A Python backend microservice using **FastAPI**, **PostgreSQL**, and **async programming** that allows users to:

- Upload a document
- Ask questions about it
- Receive a simulated LLM-generated answer asynchronously

---

## 🧰 Tech Stack

- Python 3.9+
- FastAPI
- SQLAlchemy (Async)
- PostgreSQL
- asyncio
- Pydantic

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
https://github.com/manoj8260/FASTAPI-ASGI.git
```
### 2. Create Virtual Environment & Install Dependencies
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```
### 3. Set Up Environment Variables
```bash
Copy .env.example to .env:
Then edit the .env file and update your PostgreSQL credentials:
DATABASE_URL=postgresql+asyncpg://postgres:your_password@localhost:5432/qa_db

```
##🚀 How to Run the App Locally
 Make sure your PostgreSQL server is running.

1.Then start the FastAPI app with:

```bash

uvicorn app.main:app --reload
```
2.📤 Upload a Document
POST /documents/

Request Body:

```json
{
  "title": "FastAPI Notes",
  "content": "FastAPI is a modern, fast Python web framework."
}
```
3.❓  Ask a Question About a Document
POST /documents/{document_id}/question

Request Body:
```
json
{
  "question": "What is FastAPI?"
}
```
✅ Response:
```
json
{
  "id": 1,
  "question": "What is FastAPI?",
  "answer": null,
  "status": "pending",
  "created_at": "2025-07-28T..."
}
```
4.⏳ Retrieve Answer
After ~5 seconds...

GET /questions/{question_id}

✅ Response:
```
json
{
  "id": 1,
  "question": "What is FastAPI?",
  "answer": "This is a generated answer to your question: What is FastAPI?",
  "status": "answered",
  "created_at": "2025-07-28T..."
}
```
5.❤️  Health Check
GET /health

✅ Response:
```
json
{ "status": "ok" }
```
## 📁 Project Structure
```
app/
├── main.py          # FastAPI app entry
├── config.py        # env config
├── database.py      # async DB connection
├── models.py        # SQLAlchemy models
├── schemas.py       # Pydantic schemas
├── services.py      # DB + async logic
└── api/
    ├── document.py  # document endpoints
    └── question.py  # question endpoints


