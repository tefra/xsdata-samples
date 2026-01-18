from __future__ import annotations

from dataclasses import dataclass

from .journey_version_structure import JourneyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleJourneyAbstract(JourneyVersionStructure):
    class Meta:
        name = "VehicleJourney_"
        namespace = "http://www.netex.org.uk/netex"
