from __future__ import annotations

from dataclasses import dataclass

from .t_script_task import TScriptTask

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class ScriptTask(TScriptTask):
    class Meta:
        name = "scriptTask"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
