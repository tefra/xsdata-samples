from dataclasses import dataclass
from .t_process import TProcess

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class Process(TProcess):
    class Meta:
        name = "process"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
