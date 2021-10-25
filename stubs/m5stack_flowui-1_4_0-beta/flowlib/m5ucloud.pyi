from typing import Any

class Btn:
    def attach() -> None: ...
    def deinit() -> None: ...
    def detach() -> None: ...
    def multiBtnCb() -> None: ...
    def restart() -> None: ...
    def timerCb() -> None: ...

class BtnChild:
    def deinit() -> None: ...
    def isPressed() -> None: ...
    def isReleased() -> None: ...
    def pressFor() -> None: ...
    def restart() -> None: ...
    def upDate() -> None: ...
    def wasDoublePress() -> None: ...
    def wasPressed() -> None: ...
    def wasReleased() -> None: ...

class IP5306:
    def getBatteryLevel() -> None: ...
    def init() -> None: ...
    def isChargeFull() -> None: ...
    def isCharging() -> None: ...
    def setCharge() -> None: ...
    def setChargeVolt() -> None: ...
    def setVinMaxCurrent() -> None: ...

class M5UCloud:
    def _error() -> None: ...
    def deinit() -> None: ...
    def exec_deal() -> None: ...
    def on_data() -> None: ...
    def run() -> None: ...

class Rgb_multi:
    def deinit() -> None: ...
    def setBrightness() -> None: ...
    def setColor() -> None: ...
    def setColorAll() -> None: ...
    def setColorFrom() -> None: ...
    def setShowLock() -> None: ...
    def show() -> None: ...

class Speaker:
    def _timeout_cb() -> None: ...
    def checkInit() -> None: ...
    def setBeat() -> None: ...
    def setVolume() -> None: ...
    def sing() -> None: ...
    def tone() -> None: ...

_thread: Any
apikey: str
binascii: Any
btn: Any
btnA: Any
btnB: Any
btnC: Any

def btnText() -> None: ...
def cfgRead() -> None: ...
def cfgWrite() -> None: ...

config_normal: str

def const() -> None: ...
def core_start() -> None: ...

display: Any

def flowDeinit() -> None: ...

class flowExit: ...

gc: Any

def getP2PData() -> None: ...
def get_sd_state() -> None: ...
def hwDeinit() -> None: ...

io: Any
lcd: Any

def loopExit() -> None: ...
def loopSetIdle() -> None: ...
def loopState() -> None: ...

m5base: Any
m5uart: Any
machine: Any

def modeSet() -> None: ...

module: Any
node_id: str
os: Any
power: Any

def remoteInit() -> None: ...
def resetDefault() -> None: ...

rgb: Any

def sd_mount() -> None: ...
def sd_umount() -> None: ...
def sendP2PData() -> None: ...
def setP2PData() -> None: ...

speaker: Any

def start() -> None: ...
def startBeep() -> None: ...

sys: Any
timEx: Any
time: Any
timeSchedule: Any
time_ex: Any
timerSch: Any
uiflow: Any
unit: Any

def wait() -> None: ...
def wait_ms() -> None: ...
