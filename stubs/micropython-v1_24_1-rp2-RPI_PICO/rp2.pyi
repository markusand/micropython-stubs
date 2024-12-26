"""
Module: 'rp2' on micropython-v1.24.1-rp2-RPI_PICO
"""

# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'rp2', 'board': 'RPI_PICO', 'cpu': 'RP2040', 'mpy': 'v6.3', 'arch': 'armv6m'}
# Stubber: v1.24.0
from __future__ import annotations
from _typeshed import Incomplete

_pio_funcs: dict = {}

def asm_pio_encode(*args, **kwargs) -> Incomplete: ...
def asm_pio(*args, **kwargs) -> Incomplete: ...
def bootsel_button(*args, **kwargs) -> Incomplete: ...
def const(*args, **kwargs) -> Incomplete: ...

class PIOASMEmit:
    def in_(self, *args, **kwargs) -> Incomplete: ...
    def side(self, *args, **kwargs) -> Incomplete: ...
    def out(self, *args, **kwargs) -> Incomplete: ...
    def jmp(self, *args, **kwargs) -> Incomplete: ...
    def start_pass(self, *args, **kwargs) -> Incomplete: ...
    def wrap(self, *args, **kwargs) -> Incomplete: ...
    def word(self, *args, **kwargs) -> Incomplete: ...
    def wait(self, *args, **kwargs) -> Incomplete: ...
    def wrap_target(self, *args, **kwargs) -> Incomplete: ...
    def delay(self, *args, **kwargs) -> Incomplete: ...
    def label(self, *args, **kwargs) -> Incomplete: ...
    def irq(self, *args, **kwargs) -> Incomplete: ...
    def set(self, *args, **kwargs) -> Incomplete: ...
    def mov(self, *args, **kwargs) -> Incomplete: ...
    def push(self, *args, **kwargs) -> Incomplete: ...
    def pull(self, *args, **kwargs) -> Incomplete: ...
    def nop(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class PIOASMError(Exception): ...

class PIO:
    JOIN_TX: int = 1
    JOIN_NONE: int = 0
    JOIN_RX: int = 2
    SHIFT_LEFT: int = 0
    OUT_HIGH: int = 3
    OUT_LOW: int = 2
    SHIFT_RIGHT: int = 1
    IN_LOW: int = 0
    IRQ_SM3: int = 2048
    IN_HIGH: int = 1
    IRQ_SM2: int = 1024
    IRQ_SM0: int = 256
    IRQ_SM1: int = 512
    def state_machine(self, *args, **kwargs) -> Incomplete: ...
    def remove_program(self, *args, **kwargs) -> Incomplete: ...
    def irq(self, *args, **kwargs) -> Incomplete: ...
    def add_program(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class StateMachine:
    def irq(self, *args, **kwargs) -> Incomplete: ...
    def put(self, *args, **kwargs) -> Incomplete: ...
    def restart(self, *args, **kwargs) -> Incomplete: ...
    def rx_fifo(self, *args, **kwargs) -> Incomplete: ...
    def tx_fifo(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def exec(self, *args, **kwargs) -> Incomplete: ...
    def get(self, *args, **kwargs) -> Incomplete: ...
    def active(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class DMA:
    def irq(self, *args, **kwargs) -> Incomplete: ...
    def unpack_ctrl(self, *args, **kwargs) -> Incomplete: ...
    def pack_ctrl(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...
    def config(self, *args, **kwargs) -> Incomplete: ...
    def active(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Flash:
    def readblocks(self, *args, **kwargs) -> Incomplete: ...
    def writeblocks(self, *args, **kwargs) -> Incomplete: ...
    def ioctl(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
