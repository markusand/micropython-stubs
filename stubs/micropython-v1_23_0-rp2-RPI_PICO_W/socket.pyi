"""
Module: 'socket' on micropython-v1.23.0-rp2-RPI_PICO_W
"""

# MCU: {'build': '', 'ver': '1.23.0', 'version': '1.23.0', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.3', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.23.0
from __future__ import annotations
from _typeshed import Incomplete

SOCK_STREAM: int = 1
SOCK_DGRAM: int = 2
SOCK_RAW: int = 3
SO_REUSEADDR: int = 4
SOL_SOCKET: int = 1
SO_BROADCAST: int = 32
TCP_NODELAY: int = 64
AF_INET6: int = 10
IP_DROP_MEMBERSHIP: int = 1025
AF_INET: int = 2
IP_ADD_MEMBERSHIP: int = 1024
IPPROTO_IP: int = 0
IPPROTO_TCP: int = 6

def reset(*args, **kwargs) -> Incomplete: ...
def print_pcbs(*args, **kwargs) -> Incomplete: ...
def getaddrinfo(*args, **kwargs) -> Incomplete: ...
def callback(*args, **kwargs) -> Incomplete: ...

class socket:
    def recvfrom(self, *args, **kwargs) -> Incomplete: ...
    def recv(self, *args, **kwargs) -> Incomplete: ...
    def makefile(self, *args, **kwargs) -> Incomplete: ...
    def listen(self, *args, **kwargs) -> Incomplete: ...
    def settimeout(self, *args, **kwargs) -> Incomplete: ...
    def sendall(self, *args, **kwargs) -> Incomplete: ...
    def setsockopt(self, *args, **kwargs) -> Incomplete: ...
    def setblocking(self, *args, **kwargs) -> Incomplete: ...
    def sendto(self, *args, **kwargs) -> Incomplete: ...
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
