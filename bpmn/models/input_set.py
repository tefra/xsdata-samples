from dataclasses import dataclass

from .t_input_set import TInputSet

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class InputSet(TInputSet):
    class Meta:
        name = "inputSet"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
