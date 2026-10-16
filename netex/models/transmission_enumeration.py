from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TransmissionEnumeration(StrEnum):
    AUTOMATIC = "automatic"
    AUTOMATIC4_WHEEL_DRIVE = "automatic4WheelDrive"
    MANUAL = "manual"
    MANUAL4_WHEEL_DRIVE = "manual4WheelDrive"
