from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


class TypeVehicleTransmission(Enum):
    AUTOMATIC = "Automatic"
    AUTOMATIC4_WD = "Automatic4WD"
    AUTOMATIC_AWD = "AutomaticAWD"
    MANUAL = "Manual"
    MANUAL4_WD = "Manual4WD"
    MANUAL_AWD = "ManualAWD"
