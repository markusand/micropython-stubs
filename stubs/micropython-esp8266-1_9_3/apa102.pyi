from typing import Any

class APA102:
    ORDER: Any
    def write() -> None: ...

class NeoPixel:
    ORDER: Any
    def fill() -> None: ...
    def write() -> None: ...

def apa102_write() -> None: ...
