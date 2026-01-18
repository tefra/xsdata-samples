from __future__ import annotations

from dataclasses import dataclass

from .t_global_user_task import TGlobalUserTask

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class GlobalUserTask(TGlobalUserTask):
    class Meta:
        name = "globalUserTask"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
