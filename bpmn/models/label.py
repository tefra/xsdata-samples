from dataclasses import dataclass, field
from typing import Optional
from .bounds import Bounds
from .node import Node

__NAMESPACE__ = "http://www.omg.org/spec/DD/20100524/DI"


@dataclass
class Label(Node):
    class Meta:
        namespace = "http://www.omg.org/spec/DD/20100524/DI"

    bounds: Optional[Bounds] = field(
        default=None,
        metadata={
            "name": "Bounds",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/DD/20100524/DC",
        }
    )
