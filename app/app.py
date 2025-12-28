from fastapi import FastAPI, HTTPException, File, UploadFile, Form, Depends
from app.schema import PostCreate
from app.db import Post, create_db_and_tables, create_async_engine,get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app:FastAPI):
    await create_db_and_tables()
    yield

app=FastAPI(lifespan=lifespan)

@app.post("/upload")
async def upload_file(file:UploadFile=File(...), 
                      caption:str=Form(""), 
                      session:AsyncSession=Depends(get_async_session)):
    
    pass