from __future__ import annotations

from dataclasses import dataclass

from .vehicle_meeting_place_ref_structure import (
    VehicleMeetingPlaceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehiclePoolingMeetingPlaceRefStructure(VehicleMeetingPlaceRefStructure):
    pass
