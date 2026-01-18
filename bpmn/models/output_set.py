from __future__ import annotations

from dataclasses import dataclass

from .t_output_set import TOutputSet

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class OutputSet(TOutputSet):
    class Meta:
        name = "outputSet"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
