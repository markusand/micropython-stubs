from typing import Any

class ADC:
    CORE_TEMP: int
    CORE_VBAT: int
    CORE_VREF: int
    VREF: int
    def read_u16() -> None: ...

DEEPSLEEP_RESET: int
HARD_RESET: int

class I2C:
    def init() -> None: ...
    def readfrom() -> None: ...
    def readfrom_into() -> None: ...
    def readfrom_mem() -> None: ...
    def readfrom_mem_into() -> None: ...
    def readinto() -> None: ...
    def scan() -> None: ...
    def start() -> None: ...
    def stop() -> None: ...
    def write() -> None: ...
    def writeto() -> None: ...
    def writeto_mem() -> None: ...
    def writevto() -> None: ...

PWRON_RESET: int

class Pin:
    AF1_TIM1: int
    AF1_TIM2: int
    AF2_TIM3: int
    AF2_TIM4: int
    AF2_TIM5: int
    AF3_TIM10: int
    AF3_TIM11: int
    AF3_TIM8: int
    AF3_TIM9: int
    AF4_I2C1: int
    AF4_I2C2: int
    AF5_SPI1: int
    AF5_SPI2: int
    AF7_USART1: int
    AF7_USART2: int
    AF7_USART3: int
    AF8_UART4: int
    AF8_USART6: int
    AF9_CAN1: int
    AF9_CAN2: int
    AF9_TIM12: int
    AF9_TIM13: int
    AF9_TIM14: int
    AF_OD: int
    AF_PP: int
    ALT: int
    ALT_OPEN_DRAIN: int
    ANALOG: int
    IN: int
    IRQ_FALLING: int
    IRQ_RISING: int
    OPEN_DRAIN: int
    OUT: int
    OUT_OD: int
    OUT_PP: int
    PULL_DOWN: int
    PULL_NONE: int
    PULL_UP: int
    def af() -> None: ...
    def af_list() -> None: ...
    board: Any
    cpu: Any
    def debug() -> None: ...
    def dict() -> None: ...
    def gpio() -> None: ...
    def high() -> None: ...
    def init() -> None: ...
    def irq() -> None: ...
    def low() -> None: ...
    def mapper() -> None: ...
    def mode() -> None: ...
    def name() -> None: ...
    def names() -> None: ...
    def off() -> None: ...
    def on() -> None: ...
    def pin() -> None: ...
    def port() -> None: ...
    def pull() -> None: ...
    def value() -> None: ...

class RTC:
    def calibration() -> None: ...
    def datetime() -> None: ...
    def info() -> None: ...
    def init() -> None: ...
    def wakeup() -> None: ...

SOFT_RESET: int

class SPI:
    LSB: int
    MSB: int
    def deinit() -> None: ...
    def init() -> None: ...
    def read() -> None: ...
    def readinto() -> None: ...
    def write() -> None: ...
    def write_readinto() -> None: ...

class Signal:
    def off() -> None: ...
    def on() -> None: ...
    def value() -> None: ...

class SoftI2C:
    def init() -> None: ...
    def readfrom() -> None: ...
    def readfrom_into() -> None: ...
    def readfrom_mem() -> None: ...
    def readfrom_mem_into() -> None: ...
    def readinto() -> None: ...
    def scan() -> None: ...
    def start() -> None: ...
    def stop() -> None: ...
    def write() -> None: ...
    def writeto() -> None: ...
    def writeto_mem() -> None: ...
    def writevto() -> None: ...

class SoftSPI:
    LSB: int
    MSB: int
    def deinit() -> None: ...
    def init() -> None: ...
    def read() -> None: ...
    def readinto() -> None: ...
    def write() -> None: ...
    def write_readinto() -> None: ...

class Timer:
    ONE_SHOT: int
    PERIODIC: int
    def deinit() -> None: ...
    def init() -> None: ...

class UART:
    CTS: int
    IRQ_RXIDLE: int
    RTS: int
    def any() -> None: ...
    def deinit() -> None: ...
    def init() -> None: ...
    def irq() -> None: ...
    def read() -> None: ...
    def readchar() -> None: ...
    def readinto() -> None: ...
    def readline() -> None: ...
    def sendbreak() -> None: ...
    def write() -> None: ...
    def writechar() -> None: ...

class WDT:
    def feed() -> None: ...

WDT_RESET: int

def bootloader() -> None: ...
def deepsleep() -> None: ...
def disable_irq() -> None: ...
def enable_irq() -> None: ...
def freq() -> None: ...
def idle() -> None: ...
def info() -> None: ...
def lightsleep() -> None: ...

mem16: Any
mem32: Any
mem8: Any

def reset() -> None: ...
def reset_cause() -> None: ...
def rng() -> None: ...
def sleep() -> None: ...
def soft_reset() -> None: ...
def time_pulse_us() -> None: ...
def unique_id() -> None: ...
