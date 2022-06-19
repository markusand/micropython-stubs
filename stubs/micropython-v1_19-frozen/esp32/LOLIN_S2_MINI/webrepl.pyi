from typing import Any

listen_s: Any
client_s: Any

def setup_conn(port, accept_handler): ...
def accept_conn(listen_sock) -> None: ...
def stop() -> None: ...
def start(port: int = ..., password: Any | None = ..., accept_handler=...) -> None: ...
def start_foreground(port: int = ..., password: Any | None = ...) -> None: ...
