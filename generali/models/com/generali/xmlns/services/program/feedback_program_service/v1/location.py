from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"


@dataclass
class Location:
    class Meta:
        namespace = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"

    global_location_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "GlobalLocationID",
            "type": "Element",
        }
    )
    local_location_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocalLocationID",
            "type": "Element",
        }
    )
