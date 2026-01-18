from __future__ import annotations

from dataclasses import dataclass

from .t_resource_parameter import TResourceParameter

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class ResourceParameter(TResourceParameter):
    class Meta:
        name = "resourceParameter"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
