from _typeshed import Incomplete as Incomplete

SOL_SOCKET: int
SO_BROADCAST: int
SOCK_STREAM: int
SO_REUSEADDR: int
SO_LINGER: int
SO_ERROR: int
SO_KEEPALIVE: int
AF_INET6: int
AF_UNIX: int
AF_INET: int
SOCK_RAW: int
SOCK_DGRAM: int
MSG_DONTROUTE: int
MSG_DONTWAIT: int

def sockaddr(*args, **kwargs) -> Incomplete: ...
def inet_pton(*args, **kwargs) -> Incomplete: ...
def inet_ntop(*args, **kwargs) -> Incomplete: ...
def getaddrinfo(*args, **kwargs) -> Incomplete: ...

class socket:
    def recv(self, *args, **kwargs) -> Incomplete: ...
    def makefile(self, *args, **kwargs) -> Incomplete: ...
    def listen(self, *args, **kwargs) -> Incomplete: ...
    def fileno(self, *args, **kwargs) -> Incomplete: ...
    def settimeout(self, *args, **kwargs) -> Incomplete: ...
    def recvfrom(self, *args, **kwargs) -> Incomplete: ...
    def setsockopt(self, *args, **kwargs) -> Incomplete: ...
    def setblocking(self, *args, **kwargs) -> Incomplete: ...
    def sendto(self, *args, **kwargs) -> Incomplete: ...
    def readline(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...
    def connect(self, *args, **kwargs) -> Incomplete: ...
    def send(self, *args, **kwargs) -> Incomplete: ...
    def bind(self, *args, **kwargs) -> Incomplete: ...
    def accept(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
