from .core import ble as ble, log_error as log_error, register_irq_handler as register_irq_handler
from .device import DeviceConnection as DeviceConnection
from _typeshed import Incomplete
from micropython import const as const

_IRQ_L2CAP_ACCEPT: int
_IRQ_L2CAP_CONNECT: int
_IRQ_L2CAP_DISCONNECT: int
_IRQ_L2CAP_RECV: int
_IRQ_L2CAP_SEND_READY: int
_listening: bool

def _l2cap_irq(event, data) -> None: ...
def _l2cap_shutdown() -> None: ...

class L2CAPDisconnectedError(Exception): ...
class L2CAPConnectionError(Exception): ...

class L2CAPChannel:
    _connection: Incomplete
    our_mtu: int
    peer_mtu: int
    _cid: Incomplete
    _status: int
    _stalled: bool
    _data_ready: bool
    _event: Incomplete
    def __init__(self, connection) -> None: ...
    def _assert_connected(self) -> None: ...
    async def recvinto(self, buf, timeout_ms: Incomplete | None = None): ...
    def available(self): ...
    async def send(self, buf, timeout_ms: Incomplete | None = None, chunk_size: Incomplete | None = None) -> None: ...
    async def flush(self, timeout_ms: Incomplete | None = None) -> None: ...
    async def disconnect(self, timeout_ms: int = 1000) -> None: ...
    async def disconnected(self, timeout_ms: int = 1000) -> None: ...
    async def __aenter__(self): ...
    async def __aexit__(self, exc_type, exc_val, exc_traceback) -> None: ...

async def accept(connection, psm, mtu, timeout_ms): ...
async def connect(connection, psm, mtu, timeout_ms): ...
