from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName
from .bpmnlabel import Bpmnlabel
from .labeled_shape import LabeledShape
from .participant_band_kind import ParticipantBandKind

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/DI"


@dataclass
class Bpmnshape(LabeledShape):
    class Meta:
        name = "BPMNShape"
        namespace = "http://www.omg.org/spec/BPMN/20100524/DI"

    bpmnlabel: Optional[Bpmnlabel] = field(
        default=None,
        metadata={
            "name": "BPMNLabel",
            "type": "Element",
        },
    )
    bpmn_element: Optional[QName] = field(
        default=None,
        metadata={
            "name": "bpmnElement",
            "type": "Attribute",
        },
    )
    is_horizontal: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isHorizontal",
            "type": "Attribute",
        },
    )
    is_expanded: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isExpanded",
            "type": "Attribute",
        },
    )
    is_marker_visible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isMarkerVisible",
            "type": "Attribute",
        },
    )
    is_message_visible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isMessageVisible",
            "type": "Attribute",
        },
    )
    participant_band_kind: Optional[ParticipantBandKind] = field(
        default=None,
        metadata={
            "name": "participantBandKind",
            "type": "Attribute",
        },
    )
    choreography_activity_shape: Optional[QName] = field(
        default=None,
        metadata={
            "name": "choreographyActivityShape",
            "type": "Attribute",
        },
    )
