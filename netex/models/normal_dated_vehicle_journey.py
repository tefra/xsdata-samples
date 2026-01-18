from __future__ import annotations

from dataclasses import dataclass

from .normal_dated_vehicle_journey_version_structure import (
    NormalDatedVehicleJourneyVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NormalDatedVehicleJourney(NormalDatedVehicleJourneyVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
