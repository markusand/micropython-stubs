"""
Module: 'dht' on micropython-v1.24.1-stm32-PYBV11
"""

# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'stm32', 'board': 'PYBV11', 'cpu': 'STM32F405RG', 'mpy': 'v6.3', 'arch': 'armv7emsp'}
# Stubber: v1.24.0
from __future__ import annotations
from _typeshed import Incomplete

def dht_readinto(*args, **kwargs) -> Incomplete: ...

class DHTBase:
    def measure(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class DHT22:
    def measure(self, *args, **kwargs) -> Incomplete: ...
    def temperature(self, *args, **kwargs) -> Incomplete: ...
    def humidity(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class DHT11:
    def measure(self, *args, **kwargs) -> Incomplete: ...
    def temperature(self, *args, **kwargs) -> Incomplete: ...
    def humidity(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
