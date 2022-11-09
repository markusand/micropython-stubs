# CPython core - pycopy
import io
from typing import Any, Union

class UioStream:
    _s: Any
    _is_bin: Any

    def __init__(self, s, is_bin) -> None: ...
    def write(self, data, off: Union[Any, None] = ..., sz: Union[Any, None] = ...) -> None: ...
    def __getattr__(self, attr) -> None: ...
    def __iter__(self): ...
    def __enter__(self) -> None: ...
    def __exit__(self, *args) -> None: ...

class StringIO(io.StringIO):
    def __iadd__(self, s) -> None: ...

class BytesIO(io.BytesIO):
    def __iadd__(self, s) -> None: ...

def open(name, mode: str = ..., *args, **kw): ...
