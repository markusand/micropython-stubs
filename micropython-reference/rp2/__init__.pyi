"""
Functionality specific to the RP2.

MicroPython module: https://docs.micropython.org/en/v1.24.0/library/rp2.html

The ``rp2`` module contains functions and classes specific to the RP2040, as
used in the Raspberry Pi Pico.

See the `RP2040 Python datasheet
<https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf>`_
for more information, and `pico-micropython-examples
<https://github.com/raspberrypi/pico-micropython-examples/tree/master/pio>`_
for example code.
"""

# source version: v1.24.0
# origin module:: repos/micropython/docs/library/rp2.rst
# 2024 - Jos Verlinde - PIO additions

from __future__ import annotations

from typing import Callable, Dict, List, Union, overload
from _typeshed import Incomplete
from typing_extensions import TypeAlias

from rp2.PIO import PIO
from machine import Pin

_PIO_ASM_Program: TypeAlias = Callable

class PIOASMError(Exception):
    """
    This exception is raised from `asm_pio()` or `asm_pio_encode()` if there is
    an error assembling a PIO program.
    """

def asm_pio(
    *,
    out_init: Union[Pin, List[Pin], int, List[int], None] = None,
    set_init: Union[Pin, List[Pin], int, List[int], None] = None,
    sideset_init: Union[Pin, List[Pin], int, List[int], None] = None,
    in_shiftdir=0,
    out_shiftdir=0,
    autopush=False,
    autopull=False,
    push_thresh=32,
    pull_thresh=32,
    fifo_join=PIO.JOIN_NONE,
) -> Callable[..., PIOASMEmit]:
    """
    Assemble a PIO program.

    The following parameters control the initial state of the GPIO pins, as one
    of `PIO.IN_LOW`, `PIO.IN_HIGH`, `PIO.OUT_LOW` or `PIO.OUT_HIGH`. If the
    program uses more than one pin, provide a tuple, e.g.
    ``out_init=(PIO.OUT_LOW, PIO.OUT_LOW)``.

    - *out_init* configures the pins used for ``out()`` instructions.
    - *set_init* configures the pins used for ``set()`` instructions. There can
      be at most 5.
    - *sideset_init* configures the pins used side-setting. There can be at
      most 5.

    The following parameters are used by default, but can be overridden in
    `StateMachine.init()`:

    - *in_shiftdir* is the default direction the ISR will shift, either
      `PIO.SHIFT_LEFT` or `PIO.SHIFT_RIGHT`.
    - *out_shiftdir* is the default direction the OSR will shift, either
      `PIO.SHIFT_LEFT` or `PIO.SHIFT_RIGHT`.
    - *push_thresh* is the threshold in bits before auto-push or conditional
      re-pushing is triggered.
    - *pull_thresh* is the threshold in bits before auto-pull or conditional
      re-pulling is triggered.

    The remaining parameters are:

    - *autopush* configures whether auto-push is enabled.
    - *autopull* configures whether auto-pull is enabled.
    - *fifo_join* configures whether the 4-word TX and RX FIFOs should be
      combined into a single 8-word FIFO for one direction only. The options
      are `PIO.JOIN_NONE`, `PIO.JOIN_RX` and `PIO.JOIN_TX`.
    """
    ...

def asm_pio_encode(instr, sideset_count, sideset_opt=False) -> int:
    """
    Assemble a single PIO instruction. You usually want to use `asm_pio()`
    instead.

    >>> rp2.asm_pio_encode("set(0, 1)", 0)
    57345
    """
    ...

def bootsel_button() -> int:
    # actually defined in _rp2
    """
    Temporarily turns the QSPI_SS pin into an input and reads its value,
    returning 1 for low and 0 for high.
    On a typical RP2040 board with a BOOTSEL button, a return value of 1
    indicates that the button is pressed.

    Since this function temporarily disables access to the external flash
    memory, it also temporarily disables interrupts and the other core to
    prevent them from trying to execute code from flash.
    """
    ...

class PIOASMEmit:
    """
    The PIOASMEmit class provides a comprehensive interface for constructing PIO programs,
    handling the intricacies of instruction encoding, label management, and program state.
    This allows users to build complex PIO programs in pythone, leveraging the flexibility
    and power of the PIO state machine.

    The class should not be instantiated directly, but used via the `@asm_pio` decorator.
    """

    labels: Dict
    prog: List
    wrap_used: bool
    sideset_count: int
    delay_max: int
    sideset_opt: bool
    pass_: int
    num_instr: int
    num_sideset: int

    # constants for push, pull
    noblock = 0x01
    block = 0x21

    def __init__(
        self,
        *,
        out_init: int | List | None = ...,
        set_init: int | List | None = ...,
        sideset_init: int | List | None = ...,
        in_shiftdir: int = ...,
        out_shiftdir: int = ...,
        autopush: bool = ...,
        autopull: bool = ...,
        push_thresh: int = ...,
        pull_thresh: int = ...,
        fifo_join: int = ...,
    ) -> None: ...
    @overload  # force merge
    def __getitem__(self, key): ...
    @overload  # force merge
    def __getitem__(self, key: int): ...
    #
    @overload  # force merge
    def start_pass(self, pass_) -> None:
        """The start_pass method is used to start a pass over the instructions,
        setting up the necessary state for the pass. It handles wrapping instructions
        if needed and adjusts the delay maximum based on the number of side-set bits.
        """
        ...

    @overload  # force merge
    def delay(self, delay: int):
        """rp2.PIO delay modifier.
        
        The delay method allows setting a delay for the current instruction,
        ensuring it does not exceed the maximum allowed delay.
        """

    @overload  # force merge
    def side(self, value: int):
        """rp2.PIO side modifier.
        This is a modifier which can be applied to any instruction, and is used to control side-set pin values.
        value: the value (bits) to output on the side-set pins

        When an instruction has side 0 next to it, the corresponding output is set LOW, 
        and when it has side 1 next to it, the corresponding output is set HIGH. 
        There can be up to 5 side-set pins, in which case side N is interpreted as a binary number.

        `side(0b00011)` sets the first and the second side-set pin HIGH, and the others LOW.
        """
        ...

    @overload  # force merge
    def wrap_target(self) -> None: 
        """rp2.PIO WRAP_TARGET directive.

        This directive specifies the instruction where
        execution continues due to program wrapping. This directive is invalid outside
        of a program, may only be used once within a program, and if not specified
        defaults to the start of the program
        """        
    @overload  # force merge
    def wrap(self) -> None:
        """rp2.PIO WRAP directive.

        Placed after an instruction, this directive specifies the instruction after which,
        in normal control flow (i.e. jmp with false condition, or no jmp), the program
        wraps (to .wrap_target instruction). This directive is invalid outside of a
        program, may only be used once within a program, and if not specified
        defaults to after the last program instruction.
        """
        ...
    # all below functions are PIO instructions used in the fluent notation

    @overload  # force merge
    def label(self, label: str) -> None:
        """rp2.PIO instruction.

        Labels are of the form:

        <symbol>:

        or

        PUBLIC <symbol>:

        at the start of a line
        """
        ...

    @overload  # force merge
    def word(self, instr, label: Incomplete | None = ...) -> PIOASMEmit:
        """rp2.PIO instruction.

        Stores a raw 16-bit value as an instruction in the program. This directive is
        invalid outside of a program.
        """
        ...

    @overload  # force merge
    def nop(self) -> PIOASMEmit:
        """rp2.PIO NOP instruction.

        Assembles to mov y, y. "No operation", has no particular side effect, but a useful vehicle for a side-set
        operation or an extra delay.
        """
        ...

    @overload  # force merge
    def jmp(self, condition, label: Incomplete | None = ...) -> PIOASMEmit:
        """rp2.PIO JMP instruction.

        Set program counter to Address if Condition is true, otherwise no operation.
        Delay cycles on a JMP always take effect, whether Condition is true or false, and they take place after Condition is
        evaluated and the program counter is updated.

        Parameters:

        `condition`:
        - `None` : (no condition): Always
        - `not_x` : !X: scratch X zero
        - `x_dec` : X--: scratch X non-zero, prior to decrement
        - `not_y` : !Y: scratch Y zero
        - `y_dec` : Y--: scratch Y non-zero, prior to decrement
        - `x_not_y` : X!=Y: scratch X not equal scratch Y
        - `pin` : PIN: branch on input pin
        - `not_osre` : !OSRE: output shift register not empty

        `label`: Instruction address to jump to. In the instruction encoding, this is an absolute address within the PIO
        instruction memory.

        `JMP PIN` branches on the GPIO selected by EXECCTRL_JMP_PIN, a configuration field which selects one out of the maximum
        of 32 GPIO inputs visible to a state machine, independently of the state machine’s other input mapping. The branch is
        taken if the GPIO is high.

        `!OSRE` compares the bits shifted out since the last PULL with the shift count threshold configured by SHIFTCTRL_PULL_THRESH.
        This is the same threshold used by autopull.

        `JMP X--` and `JMP Y--` always decrement scratch register X or Y, respectively. The decrement is not conditional on the
        current value of the scratch register. The branch is conditioned on the initial value of the register, i.e. before the
        decrement took place: if the register is initially nonzero, the branch is taken.
        """
        ...

    @overload  # force merge
    def wait(self, polarity: int, src: int, index: int, /) -> PIOASMEmit:
        """rp2.PIO WAIT instruction.

        Stall until some condition is met.
        Like all stalling instructions, delay cycles begin after the instruction completes. That is, if any delay cycles are present,
        they do not begin counting until after the wait condition is met.

        Parameters:

            Polarity:
                1: wait for a 1.
                0: wait for a 0.

            Source: what to wait on. Values are:
                00: GPIO: System GPIO input selected by Index. This is an absolute GPIO index, and is not affected by the state machine’s input IO mapping.
                01: PIN: Input pin selected by Index. This state machine’s input IO mapping is applied first, and then Index
            selects which of the mapped bits to wait on. In other words, the pin is selected by adding Index to the
            PINCTRL_IN_BASE configuration, modulo 32.
                10: IRQ: PIO IRQ flag selected by Index
                11: Reserved

            Index: which pin or bit to check.

        WAIT x IRQ behaves slightly differently from other WAIT sources:
        * If Polarity is 1, the selected IRQ flag is cleared by the state machine upon the wait condition being met.
        * The flag index is decoded in the same way as the IRQ index field: if the MSB is set, the state machine ID (0…3) is
        added to the IRQ index, by way of modulo-4 addition on the two LSBs. For example, state machine 2 with a flag
        value of '0x11' will wait on flag 3, and a flag value of '0x13' will wait on flag 1. This allows multiple state machines
        running the same program to synchronise with each other.
        CAUTION
        WAIT 1 IRQ x should not be used with IRQ flags presented to the interrupt controller, to avoid a race condition with a
        system interrupt handler
        """
        ...

    @overload  # force merge
    def in_(self, src: int, data) -> PIOASMEmit:
        """rp2.PIO IN instruction.

        Shift Bit count bits from Source into the Input Shift Register (ISR).
        Shift direction is configured for each state machine by SHIFTCTRL_IN_SHIFTDIR.
        Additionally, increase the input shift count by Bit count, saturating at 32.

        * Source:
            000: PINS
            001: X (scratch register X)
            010: Y (scratch register Y)
            011: NULL (all zeroes)
            100: Reserved
            101: Reserved
            110: ISR
            111: OSR
        * Bit count: How many bits to shift into the ISR. 1…32 bits, 32 is encoded as 00000.

        If automatic push is enabled, IN will also push the ISR contents to the RX FIFO if the push threshold is reached
        (SHIFTCTRL_PUSH_THRESH). IN still executes in one cycle, whether an automatic push takes place or not. The state machine
        will stall if the RX FIFO is full when an automatic push occurs. An automatic push clears the ISR contents to all-zeroes,
        and clears the input shift count.
        IN always uses the least significant Bit count bits of the source data. For example, if PINCTRL_IN_BASE is set to 5, the
        instruction IN PINS, 3 will take the values of pins 5, 6 and 7, and shift these into the ISR. First the ISR is shifted to the left
        or right to make room for the new input data, then the input data is copied into the gap this leaves. The bit order of the
        input data is not dependent on the shift direction.
        NULL can be used for shifting the ISR’s contents. For example, UARTs receive the LSB first, so must shift to the right.
        After 8 IN PINS, 1 instructions, the input serial data will occupy bits 31…24 of the ISR. An IN NULL, 24 instruction will shift
        in 24 zero bits, aligning the input data at ISR bits 7…0. Alternatively, the processor or DMA could perform a byte read
        from FIFO address + 3, which would take bits 31…24 of the FIFO contents.
        """
        ...

    @overload  # force merge
    def out(self, destination: int, bit_count: int) -> PIOASMEmit:
        """rp2.PIO OUT instruction.

        Shift Bit count bits out of the Output Shift Register (OSR), and write those bits to Destination.
        Additionally, increase the output shift count by Bit count, saturating at 32.

        Destination: (use lowercase in MicroPython)
            - 000: PINS
            - 001: X (scratch register X)
            - 010: Y (scratch register Y)
            - 011: NULL (discard data)
            - 100: PINDIRS
            - 101: PC
            - 110: ISR (also sets ISR shift counter to Bit count)
            - 111: EXEC (Execute OSR shift data as instruction)

        Bit_count:
            how many bits to shift out of the OSR. 1…32 bits, 32 is encoded as 00000.

        A 32-bit value is written to Destination: the lower Bit count bits come from the OSR, and the remainder are zeroes. This
        value is the least significant Bit count bits of the OSR if SHIFTCTRL_OUT_SHIFTDIR is to the right, otherwise it is the most
        significant bits.

        PINS and PINDIRS use the OUT pin mapping.

        If automatic pull is enabled, the OSR is automatically refilled from the TX FIFO if the pull threshold, SHIFTCTRL_PULL_THRESH,
        is reached. The output shift count is simultaneously cleared to 0. In this case, the OUT will stall if the TX FIFO is empty,
        but otherwise still executes in one cycle.

        OUT EXEC allows instructions to be included inline in the FIFO datastream. The OUT itself executes on one cycle, and the
        instruction from the OSR is executed on the next cycle. There are no restrictions on the types of instructions which can
        be executed by this mechanism. Delay cycles on the initial OUT are ignored, but the executee may insert delay cycles as
        normal.

        OUT PC behaves as an unconditional jump to an address shifted out from the OSR.
        """
        ...

    @overload  # force merge
    def push(self, value: int = ..., value2: int = ...) -> PIOASMEmit:
        """rp2.PIO PUSH instruction.

        Push the contents of the ISR into the RX FIFO, as a single 32-bit word. Clear ISR to all-zeroes.
        * IfFull: If 1, do nothing unless the total input shift count has reached its threshold, SHIFTCTRL_PUSH_THRESH (the same
        as for autopush).
        * Block: If 1, stall execution if RX FIFO is full.

        PUSH IFFULL helps to make programs more compact, like autopush. It is useful in cases where the IN would stall at an
        inappropriate time if autopush were enabled, e.g. if the state machine is asserting some external control signal at this
        point.
        The PIO assembler sets the Block bit by default. If the Block bit is not set, the PUSH does not stall on a full RX FIFO, instead
        continuing immediately to the next instruction. The FIFO state and contents are unchanged when this happens. The ISR
        is still cleared to all-zeroes, and the FDEBUG_RXSTALL flag is set (the same as a blocking PUSH or autopush to a full RX FIFO)
        to indicate data was lost.

        """
        ...

    @overload  # force merge
    def pull(self, block: int = block, timeout: int = 0) -> PIOASMEmit:
        """rp2.PIO PULL instruction.

        Load a 32-bit word from the TX FIFO into the OSR.
        * IfEmpty: If 1, do nothing unless the total output shift count has reached its threshold, SHIFTCTRL_PULL_THRESH (the
        same as for autopull).
        * Block: If 1, stall if TX FIFO is empty. If 0, pulling from an empty FIFO copies scratch X to OSR.

        Some peripherals (UART, SPI…) should halt when no data is available, and pick it up as it comes in; others (I2S) should
        clock continuously, and it is better to output placeholder or repeated data than to stop clocking. This can be achieved
        with the Block parameter.
        A nonblocking PULL on an empty FIFO has the same effect as MOV OSR, X. The program can either preload scratch register
        X with a suitable default, or execute a MOV X, OSR after each PULL NOBLOCK, so that the last valid FIFO word will be recycled
        until new data is available.

        PULL IFEMPTY is useful if an OUT with autopull would stall in an inappropriate location when the TX FIFO is empty. For
        example, a UART transmitter should not stall immediately after asserting the start bit. IfEmpty permits some of the same
        program simplifications as autopull, but the stall occurs at a controlled point in the program.

        NOTE:
        When autopull is enabled, any PULL instruction is a no-op when the OSR is full, so that the PULL instruction behaves as
        a barrier. OUT NULL, 32 can be used to explicitly discard the OSR contents. See the RP2040 Datasheet for more detail
        on autopull
        """
        ...

    @overload  # force merge
    def mov(self, dest, src, operation: int | None = None) -> PIOASMEmit:
        """rp2.PIO MOV instruction.

        Copy data from Source to Destination.

        Destination:
            - 000: PINS (Uses same pin mapping as OUT)
            - 001: X (Scratch register X)
            - 010: Y (Scratch register Y)
            - 011: Reserved
            - 100: EXEC (Execute data as instruction)
            - 101: PC
            - 110: ISR (Input shift counter is reset to 0 by this operation, i.e. empty)
            - 111: OSR (Output shift counter is reset to 0 by this operation, i.e. full)

        Operation:
            - 00: None
            - 01: Invert (bitwise complement)
            - 10: Bit-reverse
            - 11: Reserved

        Source:
            - 000: PINS (Uses same pin mapping as IN)
            - 001: X
            - 010: Y
            - 011: NULL
            - 100: Reserved
            - 101: STATUS
            - 110: ISR
            - 111: OSR

        MOV PC causes an unconditional jump. MOV EXEC has the same behaviour as OUT EXEC (Section 3.4.5), and allows register
        contents to be executed as an instruction. The MOV itself executes in 1 cycle, and the instruction in Source on the next
        cycle. Delay cycles on MOV EXEC are ignored, but the executee may insert delay cycles as normal.
        The STATUS source has a value of all-ones or all-zeroes, depending on some state machine status such as FIFO
        full/empty, configured by EXECCTRL_STATUS_SEL.

        MOV can manipulate the transferred data in limited ways, specified by the Operation argument. Invert sets each bit in
        Destination to the logical NOT of the corresponding bit in Source, i.e. 1 bits become 0 bits, and vice versa. Bit reverse sets
        each bit n in Destination to bit 31 - n in Source, assuming the bits are numbered 0 to 31.
        MOV dst, PINS reads pins using the IN pin mapping, and writes the full 32-bit value to the destination without masking.
        The LSB of the read value is the pin indicated by PINCTRL_IN_BASE, and each successive bit comes from a higher numbered pin, wrapping after 31.

        """
        ...

    @overload  # force merge
    def irq(self, mod, index: Incomplete | None = ...) -> PIOASMEmit:
        """rp2.PIO instruction.

        Set or clear the IRQ flag selected by Index argument.
        * Clear: if 1, clear the flag selected by Index, instead of raising it. If Clear is set, the Wait bit has no effect.
        * Wait: if 1, halt until the raised flag is lowered again, e.g. if a system interrupt handler has acknowledged the flag.
        * Index:

            The 3 LSBs specify an IRQ index from 0-7. This IRQ flag will be set/cleared depending on the Clear bit.

            If the MSB is set, the state machine ID (0…3) is added to the IRQ index, by way of modulo-4 addition on the
            two LSBs. For example, state machine 2 with a flag value of 0x11 will raise flag 3, and a flag value of 0x13 will raise flag 1.

        IRQ flags 4-7 are visible only to the state machines; IRQ flags 0-3 can be routed out to system level interrupts, on either
        of the PIO’s two external interrupt request lines, configured by IRQ0_INTE and IRQ1_INTE.
        The modulo addition bit allows relative addressing of 'IRQ' and 'WAIT' instructions, for synchronising state machines
        which are running the same program. Bit 2 (the third LSB) is unaffected by this addition.
        If Wait is set, Delay cycles do not begin until after the wait period elapses."""

    @overload  # force merge
    def set(self, destination: int, data) -> PIOASMEmit:
        """rp2.PIO SET instruction.

        Write immediate value Data to Destination.

        • Destination:
            000: PINS
            001: X (scratch register X) 5 LSBs are set to Data, all others cleared to 0.
            010: Y (scratch register Y) 5 LSBs are set to Data, all others cleared to 0.
            011: Reserved
            100: PINDIRS
            101: Reserved
            110: Reserved
            111: Reserved
        • Data: 5-bit immediate value to drive to pins or register.

        This can be used to assert control signals such as a clock or chip select, or to initialise loop counters. As Data is 5 bits in
        size, scratch registers can be SET to values from 0-31, which is sufficient for a 32-iteration loop.
        The mapping of SET and OUT onto pins is configured independently. They may be mapped to distinct locations, for
        example if one pin is to be used as a clock signal, and another for data. They may also be overlapping ranges of pins: a
        UART transmitter might use SET to assert start and stop bits, and OUT instructions to shift out FIFO data to the same pins.
        """
        ...
