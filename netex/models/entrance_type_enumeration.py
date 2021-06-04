from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class EntranceTypeEnumeration(Enum):
    DOOR = "door"
    DOORWAY = "doorway"
    REVOLVING_DOOR = "revolvingDoor"
    SLIDING_DOORS = "slidingDoors"
    BARRIER = "barrier"
    TICKET_BARRIER = "ticketBarrier"
    ID_BARRIER = "idBarrier"
    GATE = "gate"
    STYLE = "style"
    OTHER = "other"
