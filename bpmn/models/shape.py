from dataclasses import dataclass, field
from typing import Optional

from .bounds import Bounds
from .node import Node

__NAMESPACE__ = "http://www.omg.org/spec/DD/20100524/DI"


@dataclass
class Shape(Node):
    class Meta:
        namespace = "http://www.omg.org/spec/DD/20100524/DI"

    bounds: Bounds | None = field(
        default=None,
        metadata={
            "name": "Bounds",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/DD/20100524/DC",
            "required": True,
        },
    )
