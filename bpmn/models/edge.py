from __future__ import annotations

from dataclasses import dataclass, field

from .diagram_element import DiagramElement
from .point import Point

__NAMESPACE__ = "http://www.omg.org/spec/DD/20100524/DI"


@dataclass
class Edge(DiagramElement):
    class Meta:
        namespace = "http://www.omg.org/spec/DD/20100524/DI"

    waypoint: list[Point] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 2,
        },
    )
