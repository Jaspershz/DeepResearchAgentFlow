from fastapi import FastAPI, HTTPException, status
from app.models import QuickAnswer, DeepResearch, UserQuery
from app.services import classifier, llm_client
import uuid

app = FastAPI(
    title="Agentflow Python",
    description="Minimal FastAPI pipeline for query classification and quick responses.",
    version="0.1.0",
)


@app.post(
    "/query", response_model=QuickAnswer, status_code=status.HTTP_200_OK
)  # what's the point setting the response model?
async def query_endpoint(query: UserQuery):
    query_id = str(uuid.uuid4())
    classification = classifier.classify(UserQuery.query)
    LLMClient = llm_client.LLMClient()
    if classification == "quick":
        answer = LLMClient.generate(UserQuery.query)
        QuickAnswer.query_id = query_id

        print(answer)
        print(QuickAnswer.message_string)

    elif classification == "research":
        print(DeepResearch.message_string)
    else:
        raise HTTPException(status_code=500, detail="unexpected classification result")
