from __future__ import annotations

from dataclasses import dataclass

from .t_global_task import TGlobalTask

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class TGlobalManualTask(TGlobalTask):
    class Meta:
        name = "tGlobalManualTask"
