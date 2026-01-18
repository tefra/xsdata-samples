from __future__ import annotations

from dataclasses import dataclass

from .communication_service_version_structure import (
    CommunicationServiceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CommunicationService(CommunicationServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
