from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from .locker_type_enumeration import LockerTypeEnumeration
from .locking_type_enumeration import LockingTypeEnumeration
from .site_equipment_version_structure import SiteEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LuggageLockerEquipmentVersionStructure(SiteEquipmentVersionStructure):
    class Meta:
        name = "LuggageLockerEquipment_VersionStructure"

    number_of_lockers: None | int = field(
        default=None,
        metadata={
            "name": "NumberOfLockers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    locker_width: None | Decimal = field(
        default=None,
        metadata={
            "name": "LockerWidth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    locker_height: None | Decimal = field(
        default=None,
        metadata={
            "name": "LockerHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    locker_depth: None | Decimal = field(
        default=None,
        metadata={
            "name": "LockerDepth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    locker_type: None | LockerTypeEnumeration = field(
        default=None,
        metadata={
            "name": "LockerType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    locking_type: None | LockingTypeEnumeration = field(
        default=None,
        metadata={
            "name": "LockingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    wheelchair_accepted: None | bool = field(
        default=None,
        metadata={
            "name": "WheelchairAccepted",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    blind_accessible: None | bool = field(
        default=None,
        metadata={
            "name": "BlindAccessible",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
