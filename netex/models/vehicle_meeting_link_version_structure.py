from dataclasses import dataclass, field

from .link_version_structure import LinkVersionStructure
from .vehicle_meeting_point_ref_structure import (
    VehicleMeetingPointRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleMeetingLinkVersionStructure(LinkVersionStructure):
    class Meta:
        name = "VehicleMeetingLink_VersionStructure"

    from_point_ref: VehicleMeetingPointRefStructure | None = field(
        default=None,
        metadata={
            "name": "FromPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    to_point_ref: VehicleMeetingPointRefStructure | None = field(
        default=None,
        metadata={
            "name": "ToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
