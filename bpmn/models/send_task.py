from __future__ import annotations

from dataclasses import dataclass

from .t_send_task import TSendTask

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class SendTask(TSendTask):
    class Meta:
        name = "sendTask"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
