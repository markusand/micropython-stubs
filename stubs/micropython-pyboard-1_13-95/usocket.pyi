AF_INET: int
AF_INET6: int
SOCK_DGRAM: int
SOCK_RAW: int
SOCK_STREAM: int

def getaddrinfo() -> None: ...

class socket:
    def accept() -> None: ...
    def bind() -> None: ...
    def close() -> None: ...
    def connect() -> None: ...
    def listen() -> None: ...
    def recv() -> None: ...
    def recvfrom() -> None: ...
    def send() -> None: ...
    def sendto() -> None: ...
    def setblocking() -> None: ...
    def setsockopt() -> None: ...
    def settimeout() -> None: ...
