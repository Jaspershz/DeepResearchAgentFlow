# tests/test_classifier.py
from app.services.classifier import classify


def test_classify_short_query_is_quick():
    short_q = "What's the capital of France?"
    result = classify(short_q, demo_mode=True)
    assert result in ("quick", "research")
    # Expectation for the sprint skeleton: short factual -> quick
    assert result == "quick"


def test_classify_long_or_researchy_query_is_research():
    long_q = (
        "Produce a detailed literature research and comparative analysis of transformer "
        "architectures used in large language models since 2018, including evaluation metrics."
    )
    result = classify(long_q, demo_mode=True)
    assert result in ("quick", "research")
    # Expectation for the sprint skeleton: long/open-ended -> research
    assert result == "research"
