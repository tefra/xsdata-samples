from __future__ import annotations

from dataclasses import dataclass

from .t_rendering import TRendering

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class Rendering(TRendering):
    class Meta:
        name = "rendering"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
