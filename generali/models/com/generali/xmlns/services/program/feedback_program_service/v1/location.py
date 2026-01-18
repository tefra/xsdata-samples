from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = (
    "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"
)


@dataclass
class Location:
    class Meta:
        namespace = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"

    global_location_id: None | str = field(
        default=None,
        metadata={
            "name": "GlobalLocationID",
            "type": "Element",
            "required": True,
        },
    )
    local_location_id: None | str = field(
        default=None,
        metadata={
            "name": "LocalLocationID",
            "type": "Element",
            "required": True,
        },
    )
