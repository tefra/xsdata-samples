from __future__ import annotations

from dataclasses import dataclass, field

from .error_code_structure import ErrorCodeStructure
from .participant_ref_structure import ParticipantRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class UnknownParticipantErrorStructure(ErrorCodeStructure):
    participant_ref: None | ParticipantRefStructure = field(
        default=None,
        metadata={
            "name": "ParticipantRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
