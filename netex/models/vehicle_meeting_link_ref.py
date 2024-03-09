from dataclasses import dataclass

from .vehicle_meeting_link_ref_structure import VehicleMeetingLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleMeetingLinkRef(VehicleMeetingLinkRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
