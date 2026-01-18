from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class TLane(TBaseElement):
    class Meta:
        name = "tLane"

    partition_element: None | TBaseElement = field(
        default=None,
        metadata={
            "name": "partitionElement",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    flow_node_ref: list[str] = field(
        default_factory=list,
        metadata={
            "name": "flowNodeRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    child_lane_set: None | TLaneSet = field(
        default=None,
        metadata={
            "name": "childLaneSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    partition_element_ref: None | QName = field(
        default=None,
        metadata={
            "name": "partitionElementRef",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Lane(TLane):
    class Meta:
        name = "lane"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class TLaneSet(TBaseElement):
    class Meta:
        name = "tLaneSet"

    lane: list[Lane] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
