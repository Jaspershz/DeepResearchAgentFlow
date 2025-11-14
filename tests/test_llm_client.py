# tests/test_llm_client.py
import pytest
import asyncio

from app.services.llm_client import LLMClient


@pytest.mark.asyncio
async def test_llmclient_demo_mode_is_deterministic():
    client = LLMClient(demo_mode=True)
    prompt = "Summarize the lifecycle of a butterfly."
    out1 = await client.generate(prompt)
    out2 = await client.generate(prompt)
    # Demo-mode output must be a string and deterministic
    assert isinstance(out1, str)
    assert out1 == out2
    assert len(out1.strip()) > 0


@pytest.mark.asyncio
async def test_llmclient_handles_varied_prompts():
    client = LLMClient(demo_mode=True)
    p1 = "Short question?"
    p2 = "A different prompt that is longer and more verbose."
    r1 = await client.generate(p1)
    r2 = await client.generate(p2)
    assert isinstance(r1, str) and isinstance(r2, str)
    # They can be equal or different depending on your demo template,
    # but both must be non-empty strings.
    assert r1.strip()
    assert r2.strip()
