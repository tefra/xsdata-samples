from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from .bpmnlabel import Bpmnlabel
from .labeled_shape import LabeledShape
from .participant_band_kind import ParticipantBandKind

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/DI"


@dataclass(kw_only=True)
class Bpmnshape(LabeledShape):
    class Meta:
        name = "BPMNShape"
        namespace = "http://www.omg.org/spec/BPMN/20100524/DI"

    bpmnlabel: None | Bpmnlabel = field(
        default=None,
        metadata={
            "name": "BPMNLabel",
            "type": "Element",
        },
    )
    bpmn_element: None | QName = field(
        default=None,
        metadata={
            "name": "bpmnElement",
            "type": "Attribute",
        },
    )
    is_horizontal: None | bool = field(
        default=None,
        metadata={
            "name": "isHorizontal",
            "type": "Attribute",
        },
    )
    is_expanded: None | bool = field(
        default=None,
        metadata={
            "name": "isExpanded",
            "type": "Attribute",
        },
    )
    is_marker_visible: None | bool = field(
        default=None,
        metadata={
            "name": "isMarkerVisible",
            "type": "Attribute",
        },
    )
    is_message_visible: None | bool = field(
        default=None,
        metadata={
            "name": "isMessageVisible",
            "type": "Attribute",
        },
    )
    participant_band_kind: None | ParticipantBandKind = field(
        default=None,
        metadata={
            "name": "participantBandKind",
            "type": "Attribute",
        },
    )
    choreography_activity_shape: None | QName = field(
        default=None,
        metadata={
            "name": "choreographyActivityShape",
            "type": "Attribute",
        },
    )
