from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = (
    "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"
)


@dataclass
class LocationType:
    global_location_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "GlobalLocationID",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
            "required": True,
        },
    )
    local_location_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocalLocationID",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
            "required": True,
        },
    )
