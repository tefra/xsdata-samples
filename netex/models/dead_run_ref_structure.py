from __future__ import annotations

from dataclasses import dataclass

from .vehicle_journey_ref_structure import VehicleJourneyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeadRunRefStructure(VehicleJourneyRefStructure):
    pass
