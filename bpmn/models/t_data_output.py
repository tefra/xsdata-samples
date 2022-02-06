from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName
from .data_state import DataState
from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TDataOutput(TBaseElement):
    class Meta:
        name = "tDataOutput"

    data_state: Optional[DataState] = field(
        default=None,
        metadata={
            "name": "dataState",
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
