# CPython core - pycopy
from typing import Any

class deque:
    maxlen: Any
    flags: Any
    d: Any

    def __init__(self, iterable, maxlen, flags: int = ...) -> None: ...
    def __len__(self) -> None: ...
    def append(self, x) -> None: ...
    def popleft(self) -> None: ...
