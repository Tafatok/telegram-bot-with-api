from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from db import get_db_connection
import sqlite3
router = APIRouter()

class Chat(BaseModel):
    chat_id: int

class User(BaseModel):
    user_id: int
    name: str
    lastname: str
    chat_id: int

class Message(BaseModel):
    user_id: int
    chat_id: int
    message: str
    media_type: str = None
    media_url: str = None
    file_id: str = None


def get_db():
    connection = get_db_connection()
    try:
        yield connection
    finally:
        connection.close()

def dict_factory(cursor, row):
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}

@router.get("/api/chats")
def get_chats(db=Depends(get_db_connection)):
    db.row_factory = dict_factory
    cursor = db.cursor()
    cursor.execute("SELECT * FROM chats")
    chats = cursor.fetchall()
    return chats

@router.get("/api/chats/{user_id}")
def get_chats_for_user(user_id: int, db=Depends(get_db_connection)):
    db.row_factory = dict_factory
    cursor = db.cursor()
    cursor.execute("SELECT * FROM chats WHERE chat_id IN (SELECT chat_id FROM users WHERE user_id = ?)", (user_id,))
    chats = cursor.fetchall()
    return chats

@router.get("/api/chats/chat/{chat_id}")
def get_chat(chat_id: int, db=Depends(get_db_connection)):
    db.row_factory = dict_factory
    cursor = db.cursor()

    
    cursor.execute("SELECT * FROM chats WHERE chat_id = ?", (chat_id,))
    chat = cursor.fetchone()
    if chat is None:
        raise HTTPException(status_code=404, detail="Chat not found")

    
    cursor.execute("SELECT * FROM messages WHERE chat_id = ?", (chat_id,))
    messages = cursor.fetchall()

    
    return {"chat": chat, "messages": messages}

@router.post("/api/chats")
def create_chat(chat: Chat, db=Depends(get_db_connection)):
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO chats (chat_id) VALUES (?)", (chat.chat_id,))
        db.commit()
        return {"message": "Chat created successfully", "chat_id": chat.chat_id}
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Chat already exists")
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Failed to create chat: {e}")

@router.delete("/api/chats/{chat_id}")
def delete_chat(chat_id: int, db=Depends(get_db_connection)):
    cursor = db.cursor()
    try:
        cursor.execute("DELETE FROM users WHERE chat_id = ?", (chat_id,))
        cursor.execute("DELETE FROM messages WHERE chat_id = ?", (chat_id,))
        cursor.execute("DELETE FROM chats WHERE chat_id = ?", (chat_id,))
        db.commit()
        return {"message": "Chat and associated users and messages deleted successfully"}
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete chat: {e}")
