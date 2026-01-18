from __future__ import annotations

from dataclasses import dataclass

from .t_global_task import TGlobalTask

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class GlobalTask(TGlobalTask):
    class Meta:
        name = "globalTask"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
