from __future__ import annotations

from dataclasses import dataclass

from .t_receive_task import TReceiveTask

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class ReceiveTask(TReceiveTask):
    class Meta:
        name = "receiveTask"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
