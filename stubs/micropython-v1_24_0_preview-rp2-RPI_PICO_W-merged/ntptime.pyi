"""
Module: 'ntptime' on micropython-v1.24.0-preview-rp2-RPI_PICO_W
"""

# MCU: {'build': 'preview.136.gd1bf0eeb0', 'ver': '1.24.0-preview-preview.136.gd1bf0eeb0', 'version': '1.24.0-preview', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.3', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.23.0
from __future__ import annotations
from _typeshed import Incomplete

host: str = "pool.ntp.org"
timeout: int = 1

def settime(*args, **kwargs) -> Incomplete: ...
def time(*args, **kwargs) -> Incomplete: ...
