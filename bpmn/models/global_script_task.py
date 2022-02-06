from dataclasses import dataclass
from .t_global_script_task import TGlobalScriptTask

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class GlobalScriptTask(TGlobalScriptTask):
    class Meta:
        name = "globalScriptTask"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
