from dataclasses import dataclass, field
from typing import Optional
from .abstract_functional_service_capabilities_request import AbstractFunctionalServiceCapabilitiesRequest
from .data_object_capabilities_request import DataObjectCapabilitiesRequest
from .request_structure import RequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CapabilitiesRequestStructure(RequestStructure):
    data_object_capabilities_request: Optional[DataObjectCapabilitiesRequest] = field(
        default=None,
        metadata={
            "name": "DataObjectCapabilitiesRequest",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    abstract_functional_service_capabilities_request: Optional[AbstractFunctionalServiceCapabilitiesRequest] = field(
        default=None,
        metadata={
            "name": "AbstractFunctionalServiceCapabilitiesRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    version: str = field(
        default="2.0",
        metadata={
            "type": "Attribute",
        }
    )
