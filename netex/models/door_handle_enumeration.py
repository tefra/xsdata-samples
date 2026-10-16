from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DoorHandleEnumeration(StrEnum):
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
