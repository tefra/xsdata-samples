from dataclasses import dataclass
from .t_participant_association import TParticipantAssociation

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class ParticipantAssociation(TParticipantAssociation):
    class Meta:
        name = "participantAssociation"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
