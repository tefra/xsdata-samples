from dataclasses import dataclass, field

from .bpmnedge import Bpmnedge
from .bpmnshape import Bpmnshape
from .diagram_element import DiagramElement
from .node import Node

__NAMESPACE__ = "http://www.omg.org/spec/DD/20100524/DI"


@dataclass
class Plane(Node):
    class Meta:
        namespace = "http://www.omg.org/spec/DD/20100524/DI"

    bpmnshape: list[Bpmnshape] = field(
        default_factory=list,
        metadata={
            "name": "BPMNShape",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/DI",
        },
    )
    bpmnedge: list[Bpmnedge] = field(
        default_factory=list,
        metadata={
            "name": "BPMNEdge",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/DI",
        },
    )
    diagram_element: list[DiagramElement] = field(
        default_factory=list,
        metadata={
            "name": "DiagramElement",
            "type": "Element",
        },
    )
