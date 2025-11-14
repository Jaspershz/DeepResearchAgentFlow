# tests/test_models.py
from app.models import UserQuery, QuickAnswer
import pytest


def test_userquery_defaults_and_validation():
    # Basic instantiation
    q = UserQuery(query="What is the capital of France?")
    assert q.query == "What is the capital of France?"
    # demo_mode should default to True in the scaffold
    assert hasattr(q, "demo_mode")
    assert q.demo_mode is True


def test_quickanswer_model_shape():
    qa = QuickAnswer(query_id="01", classification="quick", answer="Paris.")
    # mode default should be "quick"
    assert qa.mode == "quick"
    assert isinstance(qa.answer, str)
    assert qa.answer == "Paris."
