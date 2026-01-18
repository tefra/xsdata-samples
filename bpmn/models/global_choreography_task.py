from __future__ import annotations

from dataclasses import dataclass

from .t_global_choreography_task import TGlobalChoreographyTask

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class GlobalChoreographyTask(TGlobalChoreographyTask):
    class Meta:
        name = "globalChoreographyTask"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
