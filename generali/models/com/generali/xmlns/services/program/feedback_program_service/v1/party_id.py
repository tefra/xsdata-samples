from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"


@dataclass
class PartyId:
    class Meta:
        name = "PartyID"
        namespace = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"

    party_guns: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartyGUNS",
            "type": "Attribute",
            "required": True,
        }
    )
    party_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartyType",
            "type": "Attribute",
            "required": True,
        }
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
