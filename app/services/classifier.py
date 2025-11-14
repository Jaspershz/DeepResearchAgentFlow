def classify(text: str, demo_mode: bool = True) -> str:
    if "research" not in text:
        return "quick"
    else:
        return "research"
