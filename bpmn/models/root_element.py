from dataclasses import dataclass

from .t_root_element import TRootElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class RootElement(TRootElement):
    class Meta:
        name = "rootElement"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
