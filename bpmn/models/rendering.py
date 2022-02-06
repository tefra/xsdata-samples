from dataclasses import dataclass
from .t_rendering import TRendering

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class Rendering(TRendering):
    class Meta:
        name = "rendering"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
