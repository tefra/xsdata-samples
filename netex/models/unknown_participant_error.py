from dataclasses import dataclass
from netex.models.unknown_participant_error_structure import UnknownParticipantErrorStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class UnknownParticipantError(UnknownParticipantErrorStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
