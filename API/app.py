from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn 
import os

from langchain_community.llms import Ollama

os.environ['OPEN_API_KEY'] = os.getenv('OPEN_API_KEY')