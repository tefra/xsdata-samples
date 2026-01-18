from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from .child_seat_enumeration import ChildSeatEnumeration
from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleModelProfileVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "VehicleModelProfile_VersionStructure"

    name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_gears: None | int = field(
        default=None,
        metadata={
            "name": "NumberOfGears",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    child_seat: None | ChildSeatEnumeration = field(
        default=None,
        metadata={
            "name": "ChildSeat",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    range_between_refuelling: None | Decimal = field(
        default=None,
        metadata={
            "name": "RangeBetweenRefuelling",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_portable: None | bool = field(
        default=None,
        metadata={
            "name": "IsPortable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
