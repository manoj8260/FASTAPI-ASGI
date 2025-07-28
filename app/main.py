from fastapi import FastAPI
from app.database import engine, Base
from app.api import document, question

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(document.router, prefix="/documents", tags=["Documents"])
app.include_router(question.router, tags=["Questions"])

@app.get("/health")
async def health():
    return {"status": "ok"}
