from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from .direction_of_use_enumeration import DirectionOfUseEnumeration
from .place_equipment_version_structure import PlaceEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessEquipmentVersionStructure(PlaceEquipmentVersionStructure):
    class Meta:
        name = "AccessEquipment_VersionStructure"

    width: None | Decimal = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    height: None | Decimal = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    direction_of_use: None | DirectionOfUseEnumeration = field(
        default=None,
        metadata={
            "name": "DirectionOfUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passengers_per_minute: None | int = field(
        default=None,
        metadata={
            "name": "PassengersPerMinute",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    relative_weighting: None | int = field(
        default=None,
        metadata={
            "name": "RelativeWeighting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    safe_for_guide_dog: None | bool = field(
        default=None,
        metadata={
            "name": "SafeForGuideDog",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
