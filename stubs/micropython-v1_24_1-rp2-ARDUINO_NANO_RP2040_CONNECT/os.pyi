"""
Module: 'os' on micropython-v1.24.1-rp2-ARDUINO_NANO_RP2040_CONNECT
"""

# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'rp2', 'board': 'ARDUINO_NANO_RP2040_CONNECT', 'cpu': 'RP2040', 'mpy': 'v6.3', 'arch': 'armv6m'}
# Stubber: v1.24.0
from __future__ import annotations
from _typeshed import Incomplete

sep: str = "/"

def rmdir(*args, **kwargs) -> Incomplete: ...
def stat(*args, **kwargs) -> Incomplete: ...
def urandom(*args, **kwargs) -> Incomplete: ...
def rename(*args, **kwargs) -> Incomplete: ...
def mount(*args, **kwargs) -> Incomplete: ...
def uname(*args, **kwargs) -> Incomplete: ...
def unlink(*args, **kwargs) -> Incomplete: ...
def statvfs(*args, **kwargs) -> Incomplete: ...
def umount(*args, **kwargs) -> Incomplete: ...
def sync(*args, **kwargs) -> Incomplete: ...
def mkdir(*args, **kwargs) -> Incomplete: ...
def dupterm(*args, **kwargs) -> Incomplete: ...
def chdir(*args, **kwargs) -> Incomplete: ...
def remove(*args, **kwargs) -> Incomplete: ...
def dupterm_notify(*args, **kwargs) -> Incomplete: ...
def listdir(*args, **kwargs) -> Incomplete: ...
def ilistdir(*args, **kwargs) -> Incomplete: ...
def getcwd(*args, **kwargs) -> Incomplete: ...

class VfsFat:
    def rename(self, *args, **kwargs) -> Incomplete: ...
    def mkfs(self, *args, **kwargs) -> Incomplete: ...
    def mount(self, *args, **kwargs) -> Incomplete: ...
    def statvfs(self, *args, **kwargs) -> Incomplete: ...
    def rmdir(self, *args, **kwargs) -> Incomplete: ...
    def stat(self, *args, **kwargs) -> Incomplete: ...
    def umount(self, *args, **kwargs) -> Incomplete: ...
    def remove(self, *args, **kwargs) -> Incomplete: ...
    def mkdir(self, *args, **kwargs) -> Incomplete: ...
    def open(self, *args, **kwargs) -> Incomplete: ...
    def ilistdir(self, *args, **kwargs) -> Incomplete: ...
    def chdir(self, *args, **kwargs) -> Incomplete: ...
    def getcwd(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class VfsLfs2:
    def rename(self, *args, **kwargs) -> Incomplete: ...
    def mkfs(self, *args, **kwargs) -> Incomplete: ...
    def mount(self, *args, **kwargs) -> Incomplete: ...
    def statvfs(self, *args, **kwargs) -> Incomplete: ...
    def rmdir(self, *args, **kwargs) -> Incomplete: ...
    def stat(self, *args, **kwargs) -> Incomplete: ...
    def umount(self, *args, **kwargs) -> Incomplete: ...
    def remove(self, *args, **kwargs) -> Incomplete: ...
    def mkdir(self, *args, **kwargs) -> Incomplete: ...
    def open(self, *args, **kwargs) -> Incomplete: ...
    def ilistdir(self, *args, **kwargs) -> Incomplete: ...
    def chdir(self, *args, **kwargs) -> Incomplete: ...
    def getcwd(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
