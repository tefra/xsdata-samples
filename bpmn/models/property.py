from dataclasses import dataclass
from .t_property import TProperty

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class Property(TProperty):
    class Meta:
        name = "property"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
