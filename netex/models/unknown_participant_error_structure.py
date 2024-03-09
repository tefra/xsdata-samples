from dataclasses import dataclass, field
from typing import Optional

from .error_code_structure import ErrorCodeStructure
from .participant_ref_structure import ParticipantRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class UnknownParticipantErrorStructure(ErrorCodeStructure):
    participant_ref: Optional[ParticipantRefStructure] = field(
        default=None,
        metadata={
            "name": "ParticipantRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
