from __future__ import annotations

from dataclasses import dataclass

from .service_journey_interchange_ref_structure import (
    ServiceJourneyInterchangeRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceJourneyInterchangeRef(ServiceJourneyInterchangeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
