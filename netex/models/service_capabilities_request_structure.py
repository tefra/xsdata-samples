from dataclasses import dataclass, field
from typing import Optional
from .abstract_service_request_structure import AbstractServiceRequestStructure
from .extensions_1 import Extensions1

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ServiceCapabilitiesRequestStructure(AbstractServiceRequestStructure):
    participant_permissions: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ParticipantPermissions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    version: str = field(
        default="2.0",
        metadata={
            "type": "Attribute",
        },
    )
