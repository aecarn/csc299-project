def inc(n: int) -> int:
    return n + 1

# Import the CLI main() from our app module
from .app import main as _app_main

def main():
    """Entry point for uv run tasks3"""
    _app_main()
# tasks3/src/tasks3/__init__.py