from . import core as core
from _typeshed import Incomplete
from collections.abc import Generator

class Stream:
    s: Incomplete
    e: Incomplete
    out_buf: bytes
    def __init__(self, s, e=...) -> None: ...
    def get_extra_info(self, v): ...
    async def __aenter__(self): ...
    async def __aexit__(self, exc_type, exc, tb) -> None: ...
    def close(self) -> None: ...
    async def wait_closed(self) -> None: ...
    async def read(self, n) -> Generator[Incomplete, None, Incomplete]: ...
    async def readinto(self, buf) -> Generator[Incomplete, None, Incomplete]: ...
    async def readexactly(self, n) -> Generator[Incomplete, None, Incomplete]: ...
    async def readline(self) -> Generator[Incomplete, None, Incomplete]: ...
    def write(self, buf) -> None: ...
    async def drain(self) -> Generator[Incomplete, None, None]: ...

StreamReader = Stream
StreamWriter = Stream

async def open_connection(host, port) -> Generator[Incomplete, None, Incomplete]: ...

class Server:
    async def __aenter__(self): ...
    async def __aexit__(self, exc_type, exc, tb) -> None: ...
    def close(self) -> None: ...
    async def wait_closed(self) -> None: ...
    async def _serve(self, s, cb) -> Generator[Incomplete, None, None]: ...

async def start_server(cb, host, port, backlog: int = ...): ...
async def stream_awrite(self, buf, off: int = ..., sz: int = ...) -> None: ...
