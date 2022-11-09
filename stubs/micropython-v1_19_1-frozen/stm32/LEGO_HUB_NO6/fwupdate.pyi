# Micropython 1.19.1 frozen stubs
from _typeshed import Incomplete

VFS_FAT: int
VFS_LFS1: int
VFS_LFS2: int
_ELEM_TYPE_END: Incomplete
_ELEM_TYPE_MOUNT: Incomplete
_ELEM_TYPE_FSLOAD: Incomplete
_ELEM_TYPE_STATUS: Incomplete

def check_mem_contains(addr, buf): ...
def dfu_read(filename): ...

class Flash:
    _FLASH_KEY1: int
    _FLASH_KEY2: int
    addressof: Incomplete
    _keyr: Incomplete
    _sr: Incomplete
    _sr_busy: Incomplete
    _cr: Incomplete
    _cr_lock: Incomplete
    _cr_init_erase: Incomplete
    _cr_start_erase: Incomplete
    _cr_init_write: Incomplete
    _cr_flush: Incomplete
    _write_multiple: int
    sector0_size: Incomplete
    def __init__(self): ...
    def wait_not_busy(self) -> None: ...
    def unlock(self) -> None: ...
    def lock(self) -> None: ...
    def erase_sector(self, sector) -> None: ...
    def write(self, addr, buf) -> None: ...

def update_mboot(filename) -> None: ...
def _create_element(kind, body): ...
def update_app_elements(
    filename, fs_base, fs_len, fs_type=..., fs_blocksize: int = ..., status_addr: Incomplete | None = ..., addr_64bit: bool = ...
): ...
def update_mpy(*args, **kwargs) -> None: ...
