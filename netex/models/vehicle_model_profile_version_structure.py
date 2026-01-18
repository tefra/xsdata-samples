from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from .child_seat_enumeration import ChildSeatEnumeration
from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleModelProfileVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "VehicleModelProfile_VersionStructure"

    name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_gears: int | None = field(
        default=None,
        metadata={
            "name": "NumberOfGears",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    child_seat: ChildSeatEnumeration | None = field(
        default=None,
        metadata={
            "name": "ChildSeat",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    range_between_refuelling: Decimal | None = field(
        default=None,
        metadata={
            "name": "RangeBetweenRefuelling",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_portable: bool | None = field(
        default=None,
        metadata={
            "name": "IsPortable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
