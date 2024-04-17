from _typeshed import Incomplete

class SyncModem:
    def _after_init(self) -> None: ...
    def send(self, packet, tx_at_ms: Incomplete | None = ...): ...
    def recv(self, timeout_ms: Incomplete | None = ..., rx_length: int = ..., rx_packet: Incomplete | None = ...): ...
    def _sync_wait(self, will_irq) -> None: ...
