from __future__ import annotations

from dataclasses import dataclass, field

from .parking_area_refs_rel_structure import ParkingAreaRefsRelStructure
from .site_entrance_version_structure import SiteEntranceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingPassengerEntranceVersionStructure(SiteEntranceVersionStructure):
    class Meta:
        name = "ParkingPassengerEntrance_VersionStructure"

    areas: ParkingAreaRefsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
