from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName
from .bpmnlabel import Bpmnlabel
from .labeled_edge import LabeledEdge
from .message_visible_kind import MessageVisibleKind

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/DI"


@dataclass
class Bpmnedge(LabeledEdge):
    class Meta:
        name = "BPMNEdge"
        namespace = "http://www.omg.org/spec/BPMN/20100524/DI"

    bpmnlabel: Optional[Bpmnlabel] = field(
        default=None,
        metadata={
            "name": "BPMNLabel",
            "type": "Element",
        }
    )
    bpmn_element: Optional[QName] = field(
        default=None,
        metadata={
            "name": "bpmnElement",
            "type": "Attribute",
        }
    )
    source_element: Optional[QName] = field(
        default=None,
        metadata={
            "name": "sourceElement",
            "type": "Attribute",
        }
    )
    target_element: Optional[QName] = field(
        default=None,
        metadata={
            "name": "targetElement",
            "type": "Attribute",
        }
    )
    message_visible_kind: Optional[MessageVisibleKind] = field(
        default=None,
        metadata={
            "name": "messageVisibleKind",
            "type": "Attribute",
        }
    )
