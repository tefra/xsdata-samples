from dataclasses import dataclass

from .t_participant_multiplicity import TParticipantMultiplicity

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class ParticipantMultiplicity(TParticipantMultiplicity):
    class Meta:
        name = "participantMultiplicity"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
