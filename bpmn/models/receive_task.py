from dataclasses import dataclass
from .t_receive_task import TReceiveTask

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class ReceiveTask(TReceiveTask):
    class Meta:
        name = "receiveTask"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
