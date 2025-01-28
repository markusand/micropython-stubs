"""
Module: 'aioble.client' on micropython-v1.24.1-rp2-ARDUINO_NANO_RP2040_CONNECT
"""

# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'rp2', 'board': 'ARDUINO_NANO_RP2040_CONNECT', 'cpu': 'RP2040', 'mpy': 'v6.3', 'arch': 'armv6m'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Generator
from _typeshed import Incomplete

def register_irq_handler(*args, **kwargs) -> Incomplete: ...
def _client_irq(*args, **kwargs) -> Incomplete: ...
def const(*args, **kwargs) -> Incomplete: ...

class DeviceConnection:
    _connected: dict = {}
    def is_connected(self, *args, **kwargs) -> Incomplete: ...
    def _run_task(self, *args, **kwargs) -> Incomplete: ...
    def services(self, *args, **kwargs) -> Incomplete: ...
    def timeout(self, *args, **kwargs) -> Incomplete: ...

    l2cap_connect: Generator  ## = <generator>
    l2cap_accept: Generator  ## = <generator>
    pair: Generator  ## = <generator>
    service: Generator  ## = <generator>
    disconnect: Generator  ## = <generator>
    device_task: Generator  ## = <generator>
    disconnected: Generator  ## = <generator>
    exchange_mtu: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class GattError(Exception): ...

class ClientService:
    def characteristics(self, *args, **kwargs) -> Incomplete: ...
    def _start_discovery(self, *args, **kwargs) -> Incomplete: ...

    characteristic: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

ble: Incomplete  ## <class 'BLE'> = <BLE>

class ClientDiscover:
    def _discover_result(self, *args, **kwargs) -> Incomplete: ...
    def _discover_done(self, *args, **kwargs) -> Incomplete: ...

    _start: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class deque:
    def pop(self, *args, **kwargs) -> Incomplete: ...
    def appendleft(self, *args, **kwargs) -> Incomplete: ...
    def popleft(self, *args, **kwargs) -> Incomplete: ...
    def extend(self, *args, **kwargs) -> Incomplete: ...
    def append(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class ClientDescriptor:
    def _read_result(self, *args, **kwargs) -> Incomplete: ...
    def _read_done(self, *args, **kwargs) -> Incomplete: ...
    def _write_done(self, *args, **kwargs) -> Incomplete: ...
    def _register_with_connection(self, *args, **kwargs) -> Incomplete: ...
    def _start_discovery(self, *args, **kwargs) -> Incomplete: ...
    def _check(self, *args, **kwargs) -> Incomplete: ...
    def _find(self, *args, **kwargs) -> Incomplete: ...
    def _connection(self, *args, **kwargs) -> Incomplete: ...

    write: Generator  ## = <generator>
    read: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class BaseClientCharacteristic:
    def _write_done(self, *args, **kwargs) -> Incomplete: ...
    def _read_done(self, *args, **kwargs) -> Incomplete: ...
    def _read_result(self, *args, **kwargs) -> Incomplete: ...
    def _register_with_connection(self, *args, **kwargs) -> Incomplete: ...
    def _find(self, *args, **kwargs) -> Incomplete: ...
    def _check(self, *args, **kwargs) -> Incomplete: ...

    write: Generator  ## = <generator>
    read: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class ClientCharacteristic:
    def _on_notify(self, *args, **kwargs) -> Incomplete: ...
    def _register_with_connection(self, *args, **kwargs) -> Incomplete: ...
    def _on_indicate(self, *args, **kwargs) -> Incomplete: ...
    def _read_result(self, *args, **kwargs) -> Incomplete: ...
    def _on_notify_indicate(self, *args, **kwargs) -> Incomplete: ...
    def _read_done(self, *args, **kwargs) -> Incomplete: ...
    def _start_discovery(self, *args, **kwargs) -> Incomplete: ...
    def descriptors(self, *args, **kwargs) -> Incomplete: ...
    def _write_done(self, *args, **kwargs) -> Incomplete: ...
    def _find(self, *args, **kwargs) -> Incomplete: ...
    def _check(self, *args, **kwargs) -> Incomplete: ...
    def _connection(self, *args, **kwargs) -> Incomplete: ...

    subscribe: Generator  ## = <generator>
    indicated: Generator  ## = <generator>
    notified: Generator  ## = <generator>
    descriptor: Generator  ## = <generator>
    read: Generator  ## = <generator>
    write: Generator  ## = <generator>
    _notified_indicated: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...
