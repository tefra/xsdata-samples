from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName
from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TInputOutputBinding(TBaseElement):
    class Meta:
        name = "tInputOutputBinding"

    operation_ref: Optional[QName] = field(
        default=None,
        metadata={
            "name": "operationRef",
            "type": "Attribute",
            "required": True,
        },
    )
    input_data_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "inputDataRef",
            "type": "Attribute",
            "required": True,
        },
    )
    output_data_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "outputDataRef",
            "type": "Attribute",
            "required": True,
        },
    )
