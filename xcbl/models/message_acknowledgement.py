from dataclasses import dataclass, field
from typing import Optional


@dataclass(kw_only=True)
class AcknowledgementLocation:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AcknowledgementNote:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AcknowledgementReferenceNumber:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class MessageAcknowledgement:
    acknowledgement_location: Optional[AcknowledgementLocation] = field(
        default=None,
        metadata={
            "name": "AcknowledgementLocation",
            "type": "Element",
        },
    )
    acknowledgement_reference_number: Optional[
        AcknowledgementReferenceNumber
    ] = field(
        default=None,
        metadata={
            "name": "AcknowledgementReferenceNumber",
            "type": "Element",
        },
    )
    acknowledgement_note: Optional[AcknowledgementNote] = field(
        default=None,
        metadata={
            "name": "AcknowledgementNote",
            "type": "Element",
        },
    )
