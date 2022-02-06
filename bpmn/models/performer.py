from dataclasses import dataclass
from .t_performer import TPerformer

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class Performer(TPerformer):
    class Meta:
        name = "performer"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
