from dataclasses import dataclass
from .t_assignment import TAssignment

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class Assignment(TAssignment):
    class Meta:
        name = "assignment"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
