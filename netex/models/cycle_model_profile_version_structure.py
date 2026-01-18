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

    gear_type_descriotion: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "GearTypeDescriotion",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    battery: bool | None = field(
        default=None,
        metadata={
            "name": "Battery",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    lamps: bool | None = field(
        default=None,
        metadata={
            "name": "Lamps",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    helmet: bool | None = field(
        default=None,
        metadata={
            "name": "Helmet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    pump: bool | None = field(
        default=None,
        metadata={
            "name": "Pump",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    locker: bool | None = field(
        default=None,
        metadata={
            "name": "Locker",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    basket: bool | None = field(
        default=None,
        metadata={
            "name": "Basket",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    lock: bool | None = field(
        default=None,
        metadata={
            "name": "Lock",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
