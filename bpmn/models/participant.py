from dataclasses import dataclass
from .t_participant import TParticipant

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class Participant(TParticipant):
    class Meta:
        name = "participant"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
