from __future__ import annotations

from dataclasses import dataclass, field

from .script import Script
from .t_global_task import TGlobalTask

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class TGlobalScriptTask(TGlobalTask):
    class Meta:
        name = "tGlobalScriptTask"

    script: None | Script = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    script_language: None | str = field(
        default=None,
        metadata={
            "name": "scriptLanguage",
            "type": "Attribute",
        },
    )
