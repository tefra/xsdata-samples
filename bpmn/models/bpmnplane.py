from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from .plane import Plane

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/DI"


@dataclass
class Bpmnplane(Plane):
    class Meta:
        name = "BPMNPlane"
        namespace = "http://www.omg.org/spec/BPMN/20100524/DI"

    bpmn_element: None | QName = field(
        default=None,
        metadata={
            "name": "bpmnElement",
            "type": "Attribute",
        },
    )
