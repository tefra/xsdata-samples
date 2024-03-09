from dataclasses import dataclass

from .t_script import TScript

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class Script(TScript):
    class Meta:
        name = "script"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
