from typing import Any

Node = Any

def alloc_emergency_exception_buf() -> None: ...
def const() -> None: ...
def heap_lock() -> None: ...
def heap_unlock() -> None: ...
def kbd_intr() -> None: ...
def mem_info() -> None: ...
def opt_level() -> None: ...
def qstr_info() -> None: ...
def schedule() -> None: ...
def stack_use() -> None: ...
