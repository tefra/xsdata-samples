from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class TInputOutputBinding(TBaseElement):
    class Meta:
        name = "tInputOutputBinding"

    operation_ref: QName = field(
        metadata={
            "name": "operationRef",
            "type": "Attribute",
            "required": True,
        }
    )
    input_data_ref: str = field(
        metadata={
            "name": "inputDataRef",
            "type": "Attribute",
            "required": True,
        }
    )
    output_data_ref: str = field(
        metadata={
            "name": "outputDataRef",
            "type": "Attribute",
            "required": True,
        }
    )
