from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from .t_root_element import TRootElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TSignal(TRootElement):
    class Meta:
        name = "tSignal"

    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    structure_ref: None | QName = field(
        default=None,
        metadata={
            "name": "structureRef",
            "type": "Attribute",
        },
    )
