from dataclasses import dataclass

from .t_text import TText

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class Text(TText):
    class Meta:
        name = "text"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
