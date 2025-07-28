import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app import models, schemas

async def create_document(db: AsyncSession, doc: schemas.DocumentCreate):
    new_doc = models.Document(**doc.dict())
    db.add(new_doc)
    await db.commit()
    await db.refresh(new_doc)
    return new_doc

async def get_document(db: AsyncSession, doc_id: int):
    return await db.get(models.Document, doc_id)

async def create_question(db: AsyncSession, doc_id: int, q: schemas.QuestionCreate):
    question = models.Question(document_id=doc_id, question=q.question)
    db.add(question)
    await db.commit()
    await db.refresh(question)

   
    asyncio.create_task(simulate_answer(db, question.id, q.question))
    return question

async def simulate_answer(db: AsyncSession, qid: int, q: str):
    await asyncio.sleep(5)
    async with db.begin():  
        question = await db.get(models.Question, qid)
        if question:
            question.answer = f"This is a generated answer to your question: {q}"
            question.status = "answered"
            db.add(question)

async def get_question(db: AsyncSession, qid: int):
    return await db.get(models.Question, qid)
