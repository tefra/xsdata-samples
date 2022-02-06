from dataclasses import dataclass
from .t_callable_element import TCallableElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class CallableElement(TCallableElement):
    class Meta:
        name = "callableElement"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
