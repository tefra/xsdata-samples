from dataclasses import dataclass
from .t_collaboration import TCollaboration

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class Collaboration(TCollaboration):
    class Meta:
        name = "collaboration"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
