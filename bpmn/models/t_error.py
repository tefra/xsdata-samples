from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName
from .t_root_element import TRootElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TError(TRootElement):
    class Meta:
        name = "tError"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    error_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "errorCode",
            "type": "Attribute",
        }
    )
    structure_ref: Optional[QName] = field(
        default=None,
        metadata={
            "name": "structureRef",
            "type": "Attribute",
        }
    )
