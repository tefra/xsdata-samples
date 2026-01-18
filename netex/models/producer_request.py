from __future__ import annotations

from dataclasses import dataclass

from .producer_request_endpoint_structure import (
    ProducerRequestEndpointStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ProducerRequest(ProducerRequestEndpointStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
