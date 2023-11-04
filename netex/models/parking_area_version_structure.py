from dataclasses import dataclass, field
from typing import Optional, Union
from .entrance_refs_rel_structure import EntranceRefsRelStructure
from .parking_bays_rel_structure import ParkingBaysRelStructure
from .parking_component_version_structure import ParkingComponentVersionStructure
from .parking_properties import ParkingProperties
from .parking_properties_rel_structure import ParkingPropertiesRelStructure

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
    parking_properties_or_parking_properties: Optional[Union[ParkingPropertiesRelStructure, ParkingProperties]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ParkingProperties",
                    "type": ParkingProperties,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "parkingProperties",
                    "type": ParkingPropertiesRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
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
