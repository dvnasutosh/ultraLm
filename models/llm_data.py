from typing import  Literal, Type

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from pydantic import BaseModel, model_validator
from langchain_core.language_models.chat_models import BaseChatModel

from services.llms.langchain_openrouters import ChatOpenRouter

class llmClient(BaseModel):
    id:str
    client:Type[ChatGoogleGenerativeAI|ChatGroq|ChatOpenRouter]
    source:Literal['openrouter','groq','gemini']
    
    @model_validator(mode='before')
    def check_client(cls, values):
        client = values.get('client')
        if client:
            if not callable(client):
                raise ValueError('client must be callable')
            if not issubclass(client, BaseChatModel):
                raise ValueError('client must be a subclass of BaseChatModel')
        return values



llmChoiceInput=Literal['qwen Reasoning',
'deepseek r1 distilled',
'Deepseek R1',
'gemini reasoning',
'gemini 2.0 pro',
'gemini image generation',]