from dataclasses import dataclass, field
from typing import Optional

from .multilingual_string import MultilingualString
from .vehicle_model_profile_version_structure import (
    VehicleModelProfileVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CycleModelProfileVersionStructure(VehicleModelProfileVersionStructure):
    class Meta:
        name = "CycleModelProfile_VersionStructure"

    gear_type_descriotion: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "GearTypeDescriotion",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    battery: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Battery",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    lamps: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Lamps",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    helmet: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Helmet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    pump: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Pump",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    locker: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Locker",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    basket: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Basket",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    lock: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Lock",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
