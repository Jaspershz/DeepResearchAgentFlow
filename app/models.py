from pydantic import BaseModel


class UserQuery(BaseModel):
    query: str
    demo_mode: bool = True


class QuickAnswer(BaseModel):
    mode: str = "quick"
    query_id: str
    classification: str
    answer: str
    message_string: str = "Quick Answer query"
    demo_mode: bool = True


class DeepResearch(BaseModel):
    mode: str = "research"
    query_id: str
    classification: str
    answer: str
    message_string: str = "Deep research query"
    demo_mode: bool = True
