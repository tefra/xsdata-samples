from __future__ import annotations

from dataclasses import dataclass

from .t_documentation import TDocumentation

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class Documentation(TDocumentation):
    class Meta:
        name = "documentation"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
