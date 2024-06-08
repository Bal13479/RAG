from enum import Enum
from typing import Any, Dict, List

from pydantic import BaseModel


class ConversationType(str, Enum):
    RAG = "RAG"
    AUTO = "AUTO"


class ConversationClient(str, Enum):
    CLI = "CLI"
    WEB = "WEB"


class ConversationCreateResponse(BaseModel):
    id: str
    chat_history: List[Dict[str, Any]]
