"""
Module: 'umqtt.simple' on micropython-v1.24.0-preview-esp32-ESP32_GENERIC_C3
"""

# MCU: {'version': '1.24.0-preview', 'mpy': 'v6.3', 'port': 'esp32', 'board': 'ESP32_GENERIC_C3', 'family': 'micropython', 'build': 'preview.136.gd1bf0eeb0', 'arch': '', 'ver': '1.24.0-preview-preview.136.gd1bf0eeb0', 'cpu': 'ESP32C3'}
# Stubber: v1.23.0
from __future__ import annotations
from _typeshed import Incomplete

def hexlify(*args, **kwargs) -> Incomplete: ...

class MQTTException(Exception): ...

class MQTTClient:
    def set_callback(self, *args, **kwargs) -> Incomplete: ...
    def publish(self, *args, **kwargs) -> Incomplete: ...
    def ping(self, *args, **kwargs) -> Incomplete: ...
    def set_last_will(self, *args, **kwargs) -> Incomplete: ...
    def subscribe(self, *args, **kwargs) -> Incomplete: ...
    def wait_msg(self, *args, **kwargs) -> Incomplete: ...
    def disconnect(self, *args, **kwargs) -> Incomplete: ...
    def connect(self, *args, **kwargs) -> Incomplete: ...
    def check_msg(self, *args, **kwargs) -> Incomplete: ...
    def _recv_len(self, *args, **kwargs) -> Incomplete: ...
    def _send_str(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
