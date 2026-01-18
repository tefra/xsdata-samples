from __future__ import annotations

from dataclasses import dataclass

from .unknown_participant_error_structure import (
    UnknownParticipantErrorStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class UnknownParticipantError(UnknownParticipantErrorStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
