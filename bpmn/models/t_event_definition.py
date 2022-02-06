from dataclasses import dataclass
from .t_root_element import TRootElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TEventDefinition(TRootElement):
    class Meta:
        name = "tEventDefinition"
