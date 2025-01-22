import os
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import trim_messages

groq_api_key =  "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"
model = ChatGroq(model="llama3-70b-8192", groq_api_key=groq_api_key)

chat_sessions = {}

def create_new_session() -> str:
    session_id = f"session_{len(chat_sessions) + 1}"
    chat_sessions[session_id] = ChatMessageHistory()
    return session_id

def get_session_name(session_id: str) -> str:
    history = get_chat_history(session_id)
    if history:
        first_message = history[0]["content"]
        return first_message[:20]
    return session_id

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in chat_sessions:
        chat_sessions[session_id] = ChatMessageHistory()
    return chat_sessions[session_id]

def generate_response(session_id: str, user_input: str) -> str:
    history = get_session_history(session_id)
    runnable = RunnableWithMessageHistory(model, get_session_history)
    response = runnable.invoke([HumanMessage(content=user_input)], config={"configurable": {"session_id": session_id}})
    history.add_user_message(user_input)
    history.add_ai_message(response.content)
    return response.content

def create_new_session() -> str:
    session_id = f"session_{len(chat_sessions) + 1}"
    chat_sessions[session_id] = ChatMessageHistory()
    return session_id

def list_sessions() -> list:
    return list(chat_sessions.keys())

def get_chat_history(session_id: str) -> list:
    if session_id in chat_sessions:
        history = chat_sessions[session_id]
        return [
            {"type": "human", "content": msg.content} if isinstance(msg, HumanMessage) else {"type": "ai", "content": msg.content}
            for msg in history.messages
        ]
    return []
