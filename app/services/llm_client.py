class LLMClient:
    def __init__(self, demo_mode: bool = True, provider_config: dict | None = None):
        self.demo_mode = demo_mode

    async def generate(self, prompt: str, max_tokens: int = 512, **kwargs) -> str:
        if self.demo_mode:
            return "demo working..."
        else:
            return "demo not True"
