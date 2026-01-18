from __future__ import annotations

from dataclasses import dataclass

from .abstract_discovery_request_structure import (
    AbstractDiscoveryRequestStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractDiscoveryRequest(AbstractDiscoveryRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
