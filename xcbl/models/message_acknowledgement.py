from __future__ import annotations

from dataclasses import dataclass, field


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
    acknowledgement_location: AcknowledgementLocation | None = field(
        default=None,
        metadata={
            "name": "AcknowledgementLocation",
            "type": "Element",
        },
    )
    acknowledgement_reference_number: AcknowledgementReferenceNumber | None = (
        field(
            default=None,
            metadata={
                "name": "AcknowledgementReferenceNumber",
                "type": "Element",
            },
        )
    )
    acknowledgement_note: AcknowledgementNote | None = field(
        default=None,
        metadata={
            "name": "AcknowledgementNote",
            "type": "Element",
        },
    )
