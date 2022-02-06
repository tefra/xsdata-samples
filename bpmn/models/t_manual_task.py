from dataclasses import dataclass
from .t_task import TTask

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TManualTask(TTask):
    class Meta:
        name = "tManualTask"
