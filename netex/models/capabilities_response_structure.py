from __future__ import annotations

from dataclasses import dataclass, field

from .data_object_capabilities_response import DataObjectCapabilitiesResponse
from .producer_response_structure import ProducerResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CapabilitiesResponseStructure(ProducerResponseStructure):
    data_object_capabilities_response: (
        None | DataObjectCapabilitiesResponse
    ) = field(
        default=None,
        metadata={
            "name": "DataObjectCapabilitiesResponse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
