from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.policy import (
    Policy,
)

__NAMESPACE__ = (
    "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"
)


@dataclass(kw_only=True)
class Policies:
    class Meta:
        namespace = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"

    policy: Policy = field(
        metadata={
            "name": "Policy",
            "type": "Element",
            "required": True,
        }
    )
