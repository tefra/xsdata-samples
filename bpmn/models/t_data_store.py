from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName
from .data_state import DataState
from .t_root_element import TRootElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TDataStore(TRootElement):
    class Meta:
        name = "tDataStore"

    data_state: Optional[DataState] = field(
        default=None,
        metadata={
            "name": "dataState",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    capacity: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    is_unlimited: bool = field(
        default=True,
        metadata={
            "name": "isUnlimited",
            "type": "Attribute",
        },
    )
    item_subject_ref: Optional[QName] = field(
        default=None,
        metadata={
            "name": "itemSubjectRef",
            "type": "Attribute",
        },
    )
