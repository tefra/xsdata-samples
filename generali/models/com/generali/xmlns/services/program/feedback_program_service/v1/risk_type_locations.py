from dataclasses import dataclass, field
from typing import Optional
from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.location_type import LocationType

__NAMESPACE__ = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"


@dataclass
class RiskTypeLocations:
    class Meta:
        global_type = False

    location: Optional[LocationType] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
        }
    )
