from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from .data_state import DataState
from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TProperty(TBaseElement):
    class Meta:
        name = "tProperty"

    data_state: DataState | None = field(
        default=None,
        metadata={
            "name": "dataState",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    name: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    item_subject_ref: QName | None = field(
        default=None,
        metadata={
            "name": "itemSubjectRef",
            "type": "Attribute",
        },
    )
