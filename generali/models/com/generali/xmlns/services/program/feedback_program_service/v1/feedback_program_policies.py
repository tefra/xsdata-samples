from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.errors import (
    Errors,
)
from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.policies import (
    Policies,
)

__NAMESPACE__ = (
    "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"
)


@dataclass(kw_only=True)
class FeedbackProgramPolicies:
    class Meta:
        namespace = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"

    action: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    schema_location: str = field(
        metadata={
            "name": "schemaLocation",
            "type": "Attribute",
            "namespace": "http://www.w3.org/2001/XMLSchema-instance",
        }
    )
    consumer_id: str = field(
        metadata={
            "name": "ConsumerID",
            "type": "Element",
        }
    )
    transmission_id: str = field(
        metadata={
            "name": "TransmissionID",
            "type": "Element",
        }
    )
    program_id: str = field(
        metadata={
            "name": "ProgramID",
            "type": "Element",
        }
    )
    local_program_id: str = field(
        metadata={
            "name": "LocalProgramID",
            "type": "Element",
        }
    )
    policies: Policies = field(
        metadata={
            "name": "Policies",
            "type": "Element",
        }
    )
    status: str = field(
        metadata={
            "name": "Status",
            "type": "Element",
        }
    )
    errors: Errors = field(
        metadata={
            "name": "Errors",
            "type": "Element",
        }
    )
