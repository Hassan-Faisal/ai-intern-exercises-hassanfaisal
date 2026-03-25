def calculator(expression: str) -> str:
    """Simple calculator tool using safe eval."""
    try:
        # Safe evaluation for basic math only
        return str(eval(expression, {"__builtins__": {}}, {}))
    except Exception as e:
        return f"Error: {str(e)}"