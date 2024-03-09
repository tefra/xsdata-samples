from dataclasses import dataclass, field
from typing import List

from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.local_policies_type_local_policy import (
    LocalPoliciesTypeLocalPolicy,
)

__NAMESPACE__ = (
    "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"
)


@dataclass
class LocalPoliciesType:
    local_policy: List[LocalPoliciesTypeLocalPolicy] = field(
        default_factory=list,
        metadata={
            "name": "LocalPolicy",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
        },
    )
