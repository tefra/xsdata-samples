from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LockingMechanismEnumeration(StrEnum):
    NONE = "none"
    DOCK = "dock"
    IMMOBILISING_LOCK = "immobilisingLock"
    SEPARATE_LOCKING_DEVICE = "separateLockingDevice"
    OTHER = "other"
