from dataclasses import dataclass
from .t_loop_characteristics import TLoopCharacteristics

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class LoopCharacteristics(TLoopCharacteristics):
    class Meta:
        name = "loopCharacteristics"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
