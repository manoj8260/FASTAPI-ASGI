from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app import schemas, services
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.DocumentOut)
async def upload_document(doc: schemas.DocumentCreate, db: AsyncSession = Depends(get_db)):
    return await services.create_document(db, doc)

@router.get("/{doc_id}", response_model=schemas.DocumentOut)
async def get_document(doc_id: int, db: AsyncSession = Depends(get_db)):
    doc = await services.get_document(db, doc_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return doc
