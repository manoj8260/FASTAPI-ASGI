from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app import schemas, services
from app.database import get_db

router = APIRouter()

@router.post("/documents/{doc_id}/question", response_model=schemas.QuestionOut)
async def ask_question(doc_id: int, q: schemas.QuestionCreate, db: AsyncSession = Depends(get_db)):
    doc = await services.get_document(db, doc_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return await services.create_question(db, doc_id, q)

@router.get("/questions/{qid}", response_model=schemas.QuestionOut)
async def get_answer(qid: int, db: AsyncSession = Depends(get_db)):
    q = await services.get_question(db, qid)
    if not q:
        raise HTTPException(status_code=404, detail="Question not found")
    return q
