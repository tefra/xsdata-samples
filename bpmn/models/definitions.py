from dataclasses import dataclass

from .t_definitions import TDefinitions

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class Definitions(TDefinitions):
    class Meta:
        name = "definitions"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
