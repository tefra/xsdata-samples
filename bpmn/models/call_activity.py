from dataclasses import dataclass

from .t_call_activity import TCallActivity

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class CallActivity(TCallActivity):
    class Meta:
        name = "callActivity"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
