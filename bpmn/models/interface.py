from dataclasses import dataclass

from .t_interface import TInterface

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class Interface(TInterface):
    class Meta:
        name = "interface"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
