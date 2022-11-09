# CPython core - pycopy
from typing import Any

MICROPY_PY_UTIME_TICKS_PERIOD: Any
_PASSTHRU: Any
clock: Any

def sleep(t) -> None: ...
def sleep_ms(t) -> None: ...
def sleep_us(t) -> None: ...
def ticks_ms() -> None: ...
def ticks_us() -> None: ...

ticks_cpu = ticks_us

def ticks_add(t, delta) -> None: ...
def ticks_diff(a, b) -> None: ...
