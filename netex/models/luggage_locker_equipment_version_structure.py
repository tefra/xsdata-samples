from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from .locker_type_enumeration import LockerTypeEnumeration
from .locking_type_enumeration import LockingTypeEnumeration
from .site_equipment_version_structure import SiteEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LuggageLockerEquipmentVersionStructure(SiteEquipmentVersionStructure):
    class Meta:
        name = "LuggageLockerEquipment_VersionStructure"

    number_of_lockers: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfLockers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    locker_width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LockerWidth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    locker_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LockerHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    locker_depth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LockerDepth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    locker_type: Optional[LockerTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "LockerType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    locking_type: Optional[LockingTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "LockingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    wheelchair_accepted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WheelchairAccepted",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    blind_accessible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BlindAccessible",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
