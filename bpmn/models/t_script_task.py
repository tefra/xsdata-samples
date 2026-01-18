from __future__ import annotations

from dataclasses import dataclass, field

from .script import Script
from .t_task import TTask

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class TScriptTask(TTask):
    class Meta:
        name = "tScriptTask"

    script: None | Script = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    script_format: None | str = field(
        default=None,
        metadata={
            "name": "scriptFormat",
            "type": "Attribute",
        },
    )
