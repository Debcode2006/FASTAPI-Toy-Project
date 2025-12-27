from fastapi import FastAPI, HTTPException
from app.schema import PostCreate
from app.db import Post, create_db_and_tables, create_async_engine,get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app:FastAPI):
    await create_db_and_tables()
    yield

app=FastAPI(lifespan=lifespan)

text_posts = {
    1: {"title": "New Post", "content": "cool text post"},
    2: {"title": "Daily Thoughts", "content": "learning FastAPI is fun"},
    3: {"title": "Motivation", "content": "consistency beats motivation"},
    4: {"title": "Tech Life", "content": "debugging at 2 AM"},
    5: {"title": "College Life", "content": "assignments never end"},
    6: {"title": "Coding Tip", "content": "read error messages carefully"},
    7: {"title": "Random Thought", "content": "coffee improves code quality"},
    8: {"title": "Reminder", "content": "commit your code frequently"},
    9: {"title": "Progress", "content": "small steps every day"},
    10: {"title": "Success", "content": "practice makes perfect"}
}


@app.get("/posts")
def get_all_posts(limit:int=None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id:int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="post not found")
    return text_posts.get(id)


@app.post("/posts")
def create_post(post:PostCreate)->PostCreate:
    new_post={"title":post.title, "content":post.content}
    text_posts[max(text_posts.keys())+1]= new_post
    
    return new_post