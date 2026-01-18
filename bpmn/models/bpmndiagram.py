from __future__ import annotations

from dataclasses import dataclass, field

from .bpmnlabel_style import BpmnlabelStyle
from .bpmnplane import Bpmnplane
from .diagram import Diagram

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/DI"


@dataclass
class Bpmndiagram(Diagram):
    class Meta:
        name = "BPMNDiagram"
        namespace = "http://www.omg.org/spec/BPMN/20100524/DI"

    bpmnplane: None | Bpmnplane = field(
        default=None,
        metadata={
            "name": "BPMNPlane",
            "type": "Element",
            "required": True,
        },
    )
    bpmnlabel_style: list[BpmnlabelStyle] = field(
        default_factory=list,
        metadata={
            "name": "BPMNLabelStyle",
            "type": "Element",
        },
    )
