from __future__ import annotations

from dataclasses import dataclass, field

from .error_code_structure import ErrorCodeStructure
from .participant_ref_structure import ParticipantRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class UnknownSubscriberErrorStructure(ErrorCodeStructure):
    subscriber_ref: None | ParticipantRefStructure = field(
        default=None,
        metadata={
            "name": "SubscriberRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
