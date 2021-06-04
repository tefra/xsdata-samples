from dataclasses import dataclass, field
from typing import Optional
from netex.models.entrance_refs_rel_structure import EntranceRefsRelStructure
from netex.models.parking_bays_rel_structure import ParkingBaysRelStructure
from netex.models.parking_component_version_structure import ParkingComponentVersionStructure
from netex.models.parking_properties import ParkingProperties
from netex.models.parking_properties_rel_structure import ParkingPropertiesRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingAreaVersionStructure(ParkingComponentVersionStructure):
    class Meta:
        name = "ParkingArea_VersionStructure"

    total_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "TotalCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    number_of_bays_with_recharging: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfBaysWithRecharging",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_properties: Optional[ParkingProperties] = field(
        default=None,
        metadata={
            "name": "ParkingProperties",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_parking_properties: Optional[ParkingPropertiesRelStructure] = field(
        default=None,
        metadata={
            "name": "parkingProperties",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    bays: Optional[ParkingBaysRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entrances: Optional[EntranceRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
