from typing import Any

bdev: Any
start_sec: int

class FlashBdev:
    def __init__(self, *argv, **kwargs) -> None: ...
    def ioctl(self, *args) -> Any: ...
    def readblocks(self, *args) -> Any: ...
    def writeblocks(self, *args) -> Any: ...
    SEC_SIZE: int

size: int
