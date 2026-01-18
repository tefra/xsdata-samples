from __future__ import annotations

from dataclasses import dataclass

from .t_resource import TResource

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class Resource(TResource):
    class Meta:
        name = "resource"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
