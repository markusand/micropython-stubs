from typing import Any

def apa102_write(*args) -> Any: ...

class NeoPixel:
    def __init__(self, *argv, **kwargs) -> None: ...
    def write(self, *args) -> Any: ...
    def fill(self, *args) -> Any: ...
    ORDER: tuple

class APA102:
    def __init__(self, *argv, **kwargs) -> None: ...
    def write(self, *args) -> Any: ...
    def fill(self, *args) -> Any: ...
    ORDER: tuple
