from __future__ import annotations

from dataclasses import dataclass

from .t_definitions import TDefinitions

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class Definitions(TDefinitions):
    class Meta:
        name = "definitions"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
