from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.risk_type_locations import (
    RiskTypeLocations,
)

__NAMESPACE__ = (
    "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"
)


@dataclass(kw_only=True)
class RiskType:
    global_risk_id: str = field(
        metadata={
            "name": "GlobalRiskID",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
            "required": True,
        }
    )
    local_risk_id: str = field(
        metadata={
            "name": "LocalRiskID",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
            "required": True,
        }
    )
    reinsurance_agreement: None | str = field(
        default=None,
        metadata={
            "name": "ReinsuranceAgreement",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
        },
    )
    locations: None | RiskTypeLocations = field(
        default=None,
        metadata={
            "name": "Locations",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
        },
    )
