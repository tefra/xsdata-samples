from __future__ import annotations

from dataclasses import dataclass

from .vehicle_pooling_meeting_place_ref_structure import (
    VehiclePoolingMeetingPlaceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehiclePoolingMeetingPlaceRef(VehiclePoolingMeetingPlaceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
