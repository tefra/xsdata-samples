from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.party_id import (
    PartyId,
)

__NAMESPACE__ = (
    "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"
)


@dataclass
class PartyIds:
    class Meta:
        name = "PartyIDs"
        namespace = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"

    party_id: PartyId | None = field(
        default=None,
        metadata={
            "name": "PartyID",
            "type": "Element",
            "required": True,
        },
    )
