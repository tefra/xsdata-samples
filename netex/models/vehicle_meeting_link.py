from __future__ import annotations

from dataclasses import dataclass

from .vehicle_meeting_link_version_structure import (
    VehicleMeetingLinkVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleMeetingLink(VehicleMeetingLinkVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
