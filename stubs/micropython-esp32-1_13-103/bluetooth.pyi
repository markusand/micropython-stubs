from typing import Any

Node = Any

class BLE:
    def active() -> None: ...
    def config() -> None: ...
    def gap_advertise() -> None: ...
    def gap_connect() -> None: ...
    def gap_disconnect() -> None: ...
    def gap_scan() -> None: ...
    def gattc_discover_characteristics() -> None: ...
    def gattc_discover_descriptors() -> None: ...
    def gattc_discover_services() -> None: ...
    def gattc_exchange_mtu() -> None: ...
    def gattc_read() -> None: ...
    def gattc_write() -> None: ...
    def gatts_indicate() -> None: ...
    def gatts_notify() -> None: ...
    def gatts_read() -> None: ...
    def gatts_register_services() -> None: ...
    def gatts_set_buffer() -> None: ...
    def gatts_write() -> None: ...
    def irq() -> None: ...

class UUID: ...
