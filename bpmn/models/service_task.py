from __future__ import annotations

from dataclasses import dataclass

from .t_service_task import TServiceTask

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class ServiceTask(TServiceTask):
    class Meta:
        name = "serviceTask"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
