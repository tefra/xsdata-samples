from dataclasses import dataclass, field
from typing import Optional
from .script import Script
from .t_global_task import TGlobalTask

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TGlobalScriptTask(TGlobalTask):
    class Meta:
        name = "tGlobalScriptTask"

    script: Optional[Script] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        }
    )
    script_language: Optional[str] = field(
        default=None,
        metadata={
            "name": "scriptLanguage",
            "type": "Attribute",
        }
    )
