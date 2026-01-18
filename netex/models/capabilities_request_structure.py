from __future__ import annotations

from dataclasses import dataclass, field

from .data_object_capabilities_request import DataObjectCapabilitiesRequest
from .request_structure import RequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class CapabilitiesRequestStructure(RequestStructure):
    data_object_capabilities_request: None | DataObjectCapabilitiesRequest = (
        field(
            default=None,
            metadata={
                "name": "DataObjectCapabilitiesRequest",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    version: str = field(
        default="2.0",
        metadata={
            "type": "Attribute",
        },
    )
