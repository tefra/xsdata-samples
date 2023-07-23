from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


class AirSegmentSpecialUpdateAction(Enum):
    APPROVE_SCHEDULE_CHANGE = "ApproveScheduleChange"
    APPROVE_SCHEDULE_CHANGE_OVERRIDE_MCT = "ApproveScheduleChangeOverrideMCT"
