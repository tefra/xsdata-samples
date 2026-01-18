from __future__ import annotations

from dataclasses import dataclass, field

from .bounds import Bounds
from .node import Node

__NAMESPACE__ = "http://www.omg.org/spec/DD/20100524/DI"


@dataclass(kw_only=True)
class Label(Node):
    class Meta:
        namespace = "http://www.omg.org/spec/DD/20100524/DI"

    bounds: None | Bounds = field(
        default=None,
        metadata={
            "name": "Bounds",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/DD/20100524/DC",
        },
    )
