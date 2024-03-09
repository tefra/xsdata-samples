from dataclasses import dataclass

from .t_activity import TActivity

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TTask(TActivity):
    class Meta:
        name = "tTask"
