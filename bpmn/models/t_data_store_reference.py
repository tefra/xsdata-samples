from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

from .data_state import DataState
from .t_flow_element import TFlowElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TDataStoreReference(TFlowElement):
    class Meta:
        name = "tDataStoreReference"

    data_state: DataState | None = field(
        default=None,
        metadata={
            "name": "dataState",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    item_subject_ref: QName | None = field(
        default=None,
        metadata={
            "name": "itemSubjectRef",
            "type": "Attribute",
        },
    )
    data_store_ref: QName | None = field(
        default=None,
        metadata={
            "name": "dataStoreRef",
            "type": "Attribute",
        },
    )
