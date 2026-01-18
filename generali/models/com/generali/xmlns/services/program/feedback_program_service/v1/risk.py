from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.locations import (
    Locations,
)

__NAMESPACE__ = (
    "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"
)


@dataclass
class Risk:
    class Meta:
        namespace = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"

    global_risk_id: str | None = field(
        default=None,
        metadata={
            "name": "GlobalRiskID",
            "type": "Element",
            "required": True,
        },
    )
    local_risk_id: str | None = field(
        default=None,
        metadata={
            "name": "LocalRiskID",
            "type": "Element",
            "required": True,
        },
    )
    reinsurance_agreement: str | None = field(
        default=None,
        metadata={
            "name": "ReinsuranceAgreement",
            "type": "Element",
            "required": True,
        },
    )
    locations: Locations | None = field(
        default=None,
        metadata={
            "name": "Locations",
            "type": "Element",
            "required": True,
        },
    )
