from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.locations import (
    Locations,
)

__NAMESPACE__ = (
    "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"
)


@dataclass(kw_only=True)
class Risk:
    class Meta:
        namespace = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"

    global_risk_id: str = field(
        metadata={
            "name": "GlobalRiskID",
            "type": "Element",
            "required": True,
        }
    )
    local_risk_id: str = field(
        metadata={
            "name": "LocalRiskID",
            "type": "Element",
            "required": True,
        }
    )
    reinsurance_agreement: str = field(
        metadata={
            "name": "ReinsuranceAgreement",
            "type": "Element",
            "required": True,
        }
    )
    locations: Locations = field(
        metadata={
            "name": "Locations",
            "type": "Element",
            "required": True,
        }
    )
