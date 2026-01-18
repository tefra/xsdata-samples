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


@dataclass
class FeedbackProgramPolicies:
    class Meta:
        namespace = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"

    action: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    schema_location: str | None = field(
        default=None,
        metadata={
            "name": "schemaLocation",
            "type": "Attribute",
            "namespace": "http://www.w3.org/2001/XMLSchema-instance",
            "required": True,
        },
    )
    consumer_id: str | None = field(
        default=None,
        metadata={
            "name": "ConsumerID",
            "type": "Element",
            "required": True,
        },
    )
    transmission_id: str | None = field(
        default=None,
        metadata={
            "name": "TransmissionID",
            "type": "Element",
            "required": True,
        },
    )
    program_id: str | None = field(
        default=None,
        metadata={
            "name": "ProgramID",
            "type": "Element",
            "required": True,
        },
    )
    local_program_id: str | None = field(
        default=None,
        metadata={
            "name": "LocalProgramID",
            "type": "Element",
            "required": True,
        },
    )
    policies: Policies | None = field(
        default=None,
        metadata={
            "name": "Policies",
            "type": "Element",
            "required": True,
        },
    )
    status: str | None = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "required": True,
        },
    )
    errors: Errors | None = field(
        default=None,
        metadata={
            "name": "Errors",
            "type": "Element",
            "required": True,
        },
    )
