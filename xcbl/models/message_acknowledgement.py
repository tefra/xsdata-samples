from dataclasses import dataclass, field
from typing import Optional


@dataclass(kw_only=True)
class MessageAcknowledgement:
    acknowledgement_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcknowledgementLocation",
            "type": "Element",
        },
    )
    acknowledgement_reference_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcknowledgementReferenceNumber",
            "type": "Element",
        },
    )
    acknowledgement_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcknowledgementNote",
            "type": "Element",
        },
    )
