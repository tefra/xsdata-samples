from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class EntranceEnumeration(StrEnum):
    OPENING = "opening"
    OPEN_DOOR = "openDoor"
    DOOR = "door"
    SWING_DOOR = "swingDoor"
    REVOLVING_DOOR = "revolvingDoor"
    AUTOMATIC_DOOR = "automaticDoor"
    TICKET_BARRIER = "ticketBarrier"
    GATE = "gate"
    OTHER = "other"
