from dataclasses import dataclass
from .t_global_manual_task import TGlobalManualTask

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class GlobalManualTask(TGlobalManualTask):
    class Meta:
        name = "globalManualTask"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
