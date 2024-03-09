from dataclasses import dataclass

from .t_service_task import TServiceTask

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class ServiceTask(TServiceTask):
    class Meta:
        name = "serviceTask"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
