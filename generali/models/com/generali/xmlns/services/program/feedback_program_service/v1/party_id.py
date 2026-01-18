from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = (
    "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"
)


@dataclass(kw_only=True)
class PartyId:
    class Meta:
        name = "PartyID"
        namespace = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"

    party_guns: str = field(
        metadata={
            "name": "PartyGUNS",
            "type": "Attribute",
            "required": True,
        }
    )
    party_type: str = field(
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
        },
    )
