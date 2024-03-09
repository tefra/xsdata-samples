from dataclasses import dataclass

from .t_task import TTask

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class Task(TTask):
    class Meta:
        name = "task"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
