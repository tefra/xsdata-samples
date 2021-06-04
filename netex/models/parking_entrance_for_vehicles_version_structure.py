from dataclasses import dataclass, field
from typing import Optional
from netex.models.parking_area_refs_rel_structure import ParkingAreaRefsRelStructure
from netex.models.site_entrance_version_structure import SiteEntranceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingEntranceForVehiclesVersionStructure(SiteEntranceVersionStructure):
    class Meta:
        name = "ParkingEntranceForVehicles__VersionStructure"

    areas: Optional[ParkingAreaRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
