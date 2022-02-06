from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName
from .data_state import DataState
from .t_flow_element import TFlowElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TDataObject(TFlowElement):
    class Meta:
        name = "tDataObject"

    data_state: Optional[DataState] = field(
        default=None,
        metadata={
            "name": "dataState",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        }
    )
    item_subject_ref: Optional[QName] = field(
        default=None,
        metadata={
            "name": "itemSubjectRef",
            "type": "Attribute",
        }
    )
    is_collection: bool = field(
        default=False,
        metadata={
            "name": "isCollection",
            "type": "Attribute",
        }
    )
