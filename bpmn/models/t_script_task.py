from __future__ import annotations

from dataclasses import dataclass, field

from .script import Script
from .t_task import TTask

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TScriptTask(TTask):
    class Meta:
        name = "tScriptTask"

    script: Script | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    script_format: str | None = field(
        default=None,
        metadata={
            "name": "scriptFormat",
            "type": "Attribute",
        },
    )
