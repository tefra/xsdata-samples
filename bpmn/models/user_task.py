from __future__ import annotations

from dataclasses import dataclass

from .t_user_task import TUserTask

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class UserTask(TUserTask):
    class Meta:
        name = "userTask"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
