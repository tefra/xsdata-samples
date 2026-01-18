from __future__ import annotations

from dataclasses import dataclass

from .t_property import TProperty

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class Property(TProperty):
    class Meta:
        name = "property"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
