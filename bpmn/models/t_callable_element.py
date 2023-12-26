from dataclasses import dataclass, field
from typing import List, Optional
from xml.etree.ElementTree import QName
from .io_binding import IoBinding
from .io_specification import IoSpecification
from .t_root_element import TRootElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TCallableElement(TRootElement):
    class Meta:
        name = "tCallableElement"

    supported_interface_ref: List[QName] = field(
        default_factory=list,
        metadata={
            "name": "supportedInterfaceRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    io_specification: Optional[IoSpecification] = field(
        default=None,
        metadata={
            "name": "ioSpecification",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    io_binding: List[IoBinding] = field(
        default_factory=list,
        metadata={
            "name": "ioBinding",
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
