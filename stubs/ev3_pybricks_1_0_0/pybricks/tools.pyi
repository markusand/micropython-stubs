from typing import Any

class StopWatch:
    def pause() -> None: ...
    def reset() -> None: ...
    def resume() -> None: ...
    def time() -> None: ...

def builtinprint() -> None: ...
def print() -> None: ...

stderr: Any

def wait() -> None: ...
