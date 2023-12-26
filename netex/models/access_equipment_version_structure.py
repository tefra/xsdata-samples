from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from .direction_of_use_enumeration import DirectionOfUseEnumeration
from .installed_equipment_version_structure import (
    InstalledEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessEquipmentVersionStructure(InstalledEquipmentVersionStructure):
    class Meta:
        name = "AccessEquipment_VersionStructure"

    width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    direction_of_use: Optional[DirectionOfUseEnumeration] = field(
        default=None,
        metadata={
            "name": "DirectionOfUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passengers_per_minute: Optional[int] = field(
        default=None,
        metadata={
            "name": "PassengersPerMinute",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    relative_weighting: Optional[int] = field(
        default=None,
        metadata={
            "name": "RelativeWeighting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    safe_for_guide_dog: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SafeForGuideDog",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
