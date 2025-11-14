from fastapi import FastAPI, HTTPException, status
from app.models import QueryReponse, UserQuery
from app.services import classifier, llm_client
import uuid

app = FastAPI(
    title="Agentflow Python",
    description="Minimal FastAPI pipeline for query classification and quick responses.",
    version="0.1.0",
)


@app.post("/query", response_model=QueryResponse, status_code=status.HTTP_200_OK)
async def query_endpoint(query: UserQuery):
    query_id = str(uuid.uuid4())
    classification = classifier.classify(UserQuery.query)
    if classification == "quick":
        answer = llm_client.generate(UserQuery.query)
        return QueryReponse(
            query_id=query_id, classification=classification, answer=answer
        )

    elif classification == "research":
        return QueryResponse(
            query_id=query_id, classification=classification, answer=None
        )
    else:
        raise HTTPException(status_code=500, detail="unexpected classification result")
