from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.location import (
    Location,
)

__NAMESPACE__ = (
    "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"
)


@dataclass
class Locations:
    class Meta:
        namespace = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"

    location: Optional[Location] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "required": True,
        },
    )
