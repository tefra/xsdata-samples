from __future__ import annotations

from dataclasses import dataclass

from .t_error import TError

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class Error(TError):
    class Meta:
        name = "error"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
