from dataclasses import dataclass
from .diagram_element import DiagramElement

__NAMESPACE__ = "http://www.omg.org/spec/DD/20100524/DI"


@dataclass
class Node(DiagramElement):
    class Meta:
        namespace = "http://www.omg.org/spec/DD/20100524/DI"
