from dataclasses import dataclass, field
from typing import Optional

from .script import Script
from .t_task import TTask

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TScriptTask(TTask):
    class Meta:
        name = "tScriptTask"

    script: Optional[Script] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    script_format: Optional[str] = field(
        default=None,
        metadata={
            "name": "scriptFormat",
            "type": "Attribute",
        },
    )
