"""
Module: 'socket' on micropython-v1.24.1-esp32-ESP32_GENERIC_S3
"""

# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'esp32', 'board': 'ESP32_GENERIC_S3', 'cpu': 'ESP32S3', 'mpy': 'v6.3', 'arch': 'xtensawin'}
# Stubber: v1.24.0
from __future__ import annotations
from _typeshed import Incomplete

SOCK_STREAM: int = 1
SOL_SOCKET: int = 4095
SOCK_RAW: int = 3
TCP_NODELAY: int = 1
SO_REUSEADDR: int = 4
SO_BINDTODEVICE: int = 4107
SO_BROADCAST: int = 32
AF_INET6: int = 10
IPPROTO_IP: int = 0
AF_INET: int = 2
SOCK_DGRAM: int = 2
IP_ADD_MEMBERSHIP: int = 3
IPPROTO_TCP: int = 6
IPPROTO_UDP: int = 17

def getaddrinfo(*args, **kwargs) -> Incomplete: ...

class socket:
    def recvfrom(self, *args, **kwargs) -> Incomplete: ...
    def recv(self, *args, **kwargs) -> Incomplete: ...
    def makefile(self, *args, **kwargs) -> Incomplete: ...
    def listen(self, *args, **kwargs) -> Incomplete: ...
    def fileno(self, *args, **kwargs) -> Incomplete: ...
    def sendall(self, *args, **kwargs) -> Incomplete: ...
    def setsockopt(self, *args, **kwargs) -> Incomplete: ...
    def setblocking(self, *args, **kwargs) -> Incomplete: ...
    def sendto(self, *args, **kwargs) -> Incomplete: ...
    def settimeout(self, *args, **kwargs) -> Incomplete: ...
    def readline(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...
    def connect(self, *args, **kwargs) -> Incomplete: ...
    def send(self, *args, **kwargs) -> Incomplete: ...
    def bind(self, *args, **kwargs) -> Incomplete: ...
    def accept(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
