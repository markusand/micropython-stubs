from typing import Any

class CancelledError(Exception): ...

class Loop:
    def __init__(self, *argv, **kwargs) -> None: ...
    def close(self, *args) -> Any: ...
    def stop(self, *args) -> Any: ...
    def call_exception_handler(self, *args) -> Any: ...
    def create_task(self, *args) -> Any: ...
    def run_until_complete(self, *args) -> Any: ...
    def run_forever(self, *args) -> Any: ...
    def set_exception_handler(self, *args) -> Any: ...
    def get_exception_handler(self, *args) -> Any: ...
    def default_exception_handler(self, *args) -> Any: ...

class Task:
    def __init__(self, *argv, **kwargs) -> None: ...

class TaskQueue:
    def __init__(self, *argv, **kwargs) -> None: ...
    def remove(self, *args) -> Any: ...
    def peek(self, *args) -> Any: ...
    def pop_head(self, *args) -> Any: ...
    def push_head(self, *args) -> Any: ...
    def push_sorted(self, *args) -> Any: ...

def sleep(*args) -> Any: ...
def sleep_ms(*args) -> Any: ...
def ticks_add(*args) -> Any: ...
def ticks_diff(*args) -> Any: ...

wait_for: Any
gather: Any

class Event:
    def __init__(self, *argv, **kwargs) -> None: ...
    def clear(self, *args) -> Any: ...
    def set(self, *args) -> Any: ...
    def is_set(self, *args) -> Any: ...
    wait: Any

class Lock:
    def __init__(self, *argv, **kwargs) -> None: ...
    def release(self, *args) -> Any: ...
    def locked(self, *args) -> Any: ...
    acquire: Any

def ticks(*args) -> Any: ...

class TimeoutError(Exception): ...

class SingletonGenerator:
    def __init__(self, *argv, **kwargs) -> None: ...

class IOQueue:
    def __init__(self, *argv, **kwargs) -> None: ...
    def remove(self, *args) -> Any: ...
    def queue_read(self, *args) -> Any: ...
    def queue_write(self, *args) -> Any: ...
    def wait_io_event(self, *args) -> Any: ...

def create_task(*args) -> Any: ...
def run_until_complete(*args) -> Any: ...
def run(*args) -> Any: ...
def get_event_loop(*args) -> Any: ...
def current_task(*args) -> Any: ...
def new_event_loop(*args) -> Any: ...

class ThreadSafeFlag:
    def __init__(self, *argv, **kwargs) -> None: ...
    def set(self, *args) -> Any: ...
    def ioctl(self, *args) -> Any: ...
    wait: Any

def wait_for_ms(*args) -> Any: ...

class StreamReader:
    def __init__(self, *argv, **kwargs) -> None: ...
    def close(self, *args) -> Any: ...
    read: Any
    readline: Any
    def write(self, *args) -> Any: ...
    wait_closed: Any
    aclose: Any
    awrite: Any
    awritestr: Any
    def get_extra_info(self, *args) -> Any: ...
    readexactly: Any
    drain: Any

class StreamWriter:
    def __init__(self, *argv, **kwargs) -> None: ...
    def close(self, *args) -> Any: ...
    read: Any
    readline: Any
    def write(self, *args) -> Any: ...
    wait_closed: Any
    aclose: Any
    awrite: Any
    awritestr: Any
    def get_extra_info(self, *args) -> Any: ...
    readexactly: Any
    drain: Any

open_connection: Any
start_server: Any
