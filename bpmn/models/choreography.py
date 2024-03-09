from dataclasses import dataclass

from .t_choreography import TChoreography

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class Choreography(TChoreography):
    class Meta:
        name = "choreography"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
