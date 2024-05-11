from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DoorHandleEnumeration(Enum):
    NONE = "none"
    LEVER = "lever"
    BUTTON = "button"
    KNOB = "knob"
    CRASH_BAR = "crashBar"
    DOOR_HANDLE = "doorHandle"
    GRAB_RAIL = "grabRail"
    WINDOW_LEVER = "windowLever"
    VERTICAL = "vertical"
    OTHER = "other"
