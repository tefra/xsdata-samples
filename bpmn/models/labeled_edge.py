from __future__ import annotations

from dataclasses import dataclass

from .edge import Edge

__NAMESPACE__ = "http://www.omg.org/spec/DD/20100524/DI"


@dataclass(kw_only=True)
class LabeledEdge(Edge):
    class Meta:
        namespace = "http://www.omg.org/spec/DD/20100524/DI"
