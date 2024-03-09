from dataclasses import dataclass

from .t_activity import TActivity

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class Activity(TActivity):
    class Meta:
        name = "activity"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
