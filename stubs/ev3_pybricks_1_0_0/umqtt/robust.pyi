from typing import Any

class MQTTClient:
    DEBUG: Any
    DELAY: int
    def _recv_len() -> None: ...
    def _send_str() -> None: ...
    def check_msg() -> None: ...
    def connect() -> None: ...
    def delay() -> None: ...
    def disconnect() -> None: ...
    def log() -> None: ...
    def ping() -> None: ...
    publish: Any
    reconnect: Any
    def set_callback() -> None: ...
    def set_last_will() -> None: ...
    def subscribe() -> None: ...
    wait_msg: Any

simple: Any
utime: Any
