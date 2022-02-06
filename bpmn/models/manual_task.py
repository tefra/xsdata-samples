from dataclasses import dataclass
from .t_manual_task import TManualTask

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class ManualTask(TManualTask):
    class Meta:
        name = "manualTask"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
