from __future__ import annotations

from dataclasses import dataclass, field

from .multilingual_string import MultilingualString
from .vehicle_model_profile_version_structure import (
    VehicleModelProfileVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CycleModelProfileVersionStructure(VehicleModelProfileVersionStructure):
    class Meta:
        name = "CycleModelProfile_VersionStructure"

    gear_type_descriotion: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "GearTypeDescriotion",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    battery: None | bool = field(
        default=None,
        metadata={
            "name": "Battery",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    lamps: None | bool = field(
        default=None,
        metadata={
            "name": "Lamps",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    helmet: None | bool = field(
        default=None,
        metadata={
            "name": "Helmet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    pump: None | bool = field(
        default=None,
        metadata={
            "name": "Pump",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    locker: None | bool = field(
        default=None,
        metadata={
            "name": "Locker",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    basket: None | bool = field(
        default=None,
        metadata={
            "name": "Basket",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    lock: None | bool = field(
        default=None,
        metadata={
            "name": "Lock",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
