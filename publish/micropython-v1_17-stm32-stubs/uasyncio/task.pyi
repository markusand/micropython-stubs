from . import core as core
from _typeshed import Incomplete

def ph_meld(h1, h2): ...
def ph_pairing(child): ...
def ph_delete(heap, node): ...

class TaskQueue:
    heap: Incomplete
    def __init__(self) -> None: ...
    def peek(self): ...
    def push_sorted(self, v, key) -> None: ...
    def push_head(self, v) -> None: ...
    def pop_head(self): ...
    def remove(self, v) -> None: ...

class Task:
    coro: Incomplete
    data: Incomplete
    state: bool
    ph_key: int
    ph_child: Incomplete
    ph_child_last: Incomplete
    ph_next: Incomplete
    ph_rightmost_parent: Incomplete
    def __init__(self, coro, globals: Incomplete | None = ...) -> None: ...
    def __iter__(self): ...
    def __next__(self) -> None: ...
    def done(self): ...
    def cancel(self): ...
