"""
Module: 'neopixel' on micropython-v1.24.1-rp2-RPI_PICO
"""

# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'rp2', 'board': 'RPI_PICO', 'cpu': 'RP2040', 'mpy': 'v6.3', 'arch': 'armv6m'}
# Stubber: v1.24.0
from __future__ import annotations
from _typeshed import Incomplete

def bitstream(*args, **kwargs) -> Incomplete: ...

class NeoPixel:
    ORDER: tuple = ()
    def write(self, *args, **kwargs) -> Incomplete: ...
    def fill(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
