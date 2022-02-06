from dataclasses import dataclass, field
from typing import List, Optional
from xml.etree.ElementTree import QName
from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TLane(TBaseElement):
    class Meta:
        name = "tLane"

    partition_element: Optional[TBaseElement] = field(
        default=None,
        metadata={
            "name": "partitionElement",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        }
    )
    flow_node_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "flowNodeRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        }
    )
    child_lane_set: Optional["TLaneSet"] = field(
        default=None,
        metadata={
            "name": "childLaneSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    partition_element_ref: Optional[QName] = field(
        default=None,
        metadata={
            "name": "partitionElementRef",
            "type": "Attribute",
        }
    )


@dataclass
class Lane(TLane):
    class Meta:
        name = "lane"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TLaneSet(TBaseElement):
    class Meta:
        name = "tLaneSet"

    lane: List[Lane] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
