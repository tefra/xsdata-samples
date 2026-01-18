from __future__ import annotations

from dataclasses import dataclass

from .t_process import TProcess

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class Process(TProcess):
    class Meta:
        name = "process"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
