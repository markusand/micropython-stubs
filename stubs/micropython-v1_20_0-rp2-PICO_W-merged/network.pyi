from typing import Any

STA_IF: int
STAT_IDLE: int
STAT_NO_AP_FOUND: int
STAT_WRONG_PASSWORD: int
STAT_GOT_IP: int
AP_IF: int
STAT_CONNECTING: int
STAT_CONNECT_FAIL: int

def route(*args, **kwargs) -> Any: ...
def hostname(*args, **kwargs) -> Any: ...
def country(*args, **kwargs) -> Any: ...

class WLAN:
    def isconnected(self, *args, **kwargs) -> Any: ...
    def ioctl(self, *args, **kwargs) -> Any: ...
    def ifconfig(self, *args, **kwargs) -> Any: ...
    def scan(self, *args, **kwargs) -> Any: ...
    def send_ethernet(self, *args, **kwargs) -> Any: ...
    def status(self, *args, **kwargs) -> Any: ...
    def config(self, *args, **kwargs) -> Any: ...
    def active(self, *args, **kwargs) -> Any: ...
    def disconnect(self, *args, **kwargs) -> Any: ...
    def connect(self, *args, **kwargs) -> Any: ...
    def deinit(self, *args, **kwargs) -> Any: ...
    def __init__(self, *argv, **kwargs) -> None: ...
