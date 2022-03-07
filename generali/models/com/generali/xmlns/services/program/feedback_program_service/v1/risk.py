from dataclasses import dataclass, field
from typing import Optional
from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.locations import Locations

__NAMESPACE__ = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"


@dataclass
class Risk:
    class Meta:
        namespace = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"

    global_risk_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "GlobalRiskID",
            "type": "Element",
        }
    )
    local_risk_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocalRiskID",
            "type": "Element",
        }
    )
    reinsurance_agreement: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReinsuranceAgreement",
            "type": "Element",
        }
    )
    locations: Optional[Locations] = field(
        default=None,
        metadata={
            "name": "Locations",
            "type": "Element",
        }
    )
