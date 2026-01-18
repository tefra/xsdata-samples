from __future__ import annotations

from dataclasses import dataclass

from .service_journey_ref_structure import ServiceJourneyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceJourneyRef(ServiceJourneyRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
