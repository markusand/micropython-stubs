from typing import Any

def const(*args, **kwargs) -> Any: ...

class Flash:
    def __init__(self, *argv, **kwargs) -> None: ...
    def ioctl(self, *args, **kwargs) -> Any: ...
    def readblocks(self, *args, **kwargs) -> Any: ...
    def writeblocks(self, *args, **kwargs) -> Any: ...

class PIO:
    def __init__(self, *argv, **kwargs) -> None: ...
    IN_HIGH: int
    IN_LOW: int
    IRQ_SM0: int
    IRQ_SM1: int
    IRQ_SM2: int
    IRQ_SM3: int
    JOIN_NONE: int
    JOIN_RX: int
    JOIN_TX: int
    OUT_HIGH: int
    OUT_LOW: int
    SHIFT_LEFT: int
    SHIFT_RIGHT: int
    def add_program(self, *args, **kwargs) -> Any: ...
    def irq(self, *args, **kwargs) -> Any: ...
    def remove_program(self, *args, **kwargs) -> Any: ...
    def state_machine(self, *args, **kwargs) -> Any: ...

class StateMachine:
    def __init__(self, *argv, **kwargs) -> None: ...
    def exec(self, *args, **kwargs) -> Any: ...
    def get(self, *args, **kwargs) -> Any: ...
    def active(self, *args, **kwargs) -> Any: ...
    def init(self, *args, **kwargs) -> Any: ...
    def irq(self, *args, **kwargs) -> Any: ...
    def put(self, *args, **kwargs) -> Any: ...
    def restart(self, *args, **kwargs) -> Any: ...
    def rx_fifo(self, *args, **kwargs) -> Any: ...
    def tx_fifo(self, *args, **kwargs) -> Any: ...

def asm_pio_encode(*args, **kwargs) -> Any: ...
def country(*args, **kwargs) -> Any: ...
def dht_readinto(*args, **kwargs) -> Any: ...

class PIOASMError(Exception): ...

class PIOASMEmit:
    def __init__(self, *argv, **kwargs) -> None: ...
    def set(self, *args, **kwargs) -> Any: ...
    def irq(self, *args, **kwargs) -> Any: ...
    def label(self, *args, **kwargs) -> Any: ...
    def mov(self, *args, **kwargs) -> Any: ...
    def nop(self, *args, **kwargs) -> Any: ...
    def pull(self, *args, **kwargs) -> Any: ...
    def push(self, *args, **kwargs) -> Any: ...
    def wrap_target(self, *args, **kwargs) -> Any: ...
    def wrap(self, *args, **kwargs) -> Any: ...
    def word(self, *args, **kwargs) -> Any: ...
    def jmp(self, *args, **kwargs) -> Any: ...
    def wait(self, *args, **kwargs) -> Any: ...
    def in_(self, *args, **kwargs) -> Any: ...
    def out(self, *args, **kwargs) -> Any: ...
    def start_pass(self, *args, **kwargs) -> Any: ...
    def delay(self, *args, **kwargs) -> Any: ...
    def side(self, *args, **kwargs) -> Any: ...

def asm_pio(*args, **kwargs) -> Any: ...
