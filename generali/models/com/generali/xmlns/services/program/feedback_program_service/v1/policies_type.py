from dataclasses import dataclass, field
from typing import List
from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.policy import Policy

__NAMESPACE__ = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"


@dataclass
class PoliciesType:
    policy: List[Policy] = field(
        default_factory=list,
        metadata={
            "name": "Policy",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
            "min_occurs": 1,
        }
    )
