from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from .direction_of_use_enumeration import DirectionOfUseEnumeration
from .place_equipment_version_structure import PlaceEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessEquipmentVersionStructure(PlaceEquipmentVersionStructure):
    class Meta:
        name = "AccessEquipment_VersionStructure"

    width: Decimal | None = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    height: Decimal | None = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    direction_of_use: DirectionOfUseEnumeration | None = field(
        default=None,
        metadata={
            "name": "DirectionOfUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passengers_per_minute: int | None = field(
        default=None,
        metadata={
            "name": "PassengersPerMinute",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    relative_weighting: int | None = field(
        default=None,
        metadata={
            "name": "RelativeWeighting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    safe_for_guide_dog: bool | None = field(
        default=None,
        metadata={
            "name": "SafeForGuideDog",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
