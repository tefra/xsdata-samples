from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field
from decimal import Decimal

from .actual_vehicle_equipment_version_structure import (
    ActualVehicleEquipmentVersionStructure,
)
from .assistance_needed_enumeration import AssistanceNeededEnumeration
from .assisted_boarding_location_enumeration import (
    AssistedBoardingLocationEnumeration,
)
from .mobility_enumeration import MobilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessVehicleEquipmentVersionStructure(
    ActualVehicleEquipmentVersionStructure
):
    class Meta:
        name = "AccessVehicleEquipment_VersionStructure"

    low_floor: None | bool = field(
        default=None,
        metadata={
            "name": "LowFloor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    high_floor: None | bool = field(
        default=None,
        metadata={
            "name": "HighFloor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    hoist: None | bool = field(
        default=None,
        metadata={
            "name": "Hoist",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    ramp: None | bool = field(
        default=None,
        metadata={
            "name": "Ramp",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    bearing_capacity: None | Decimal = field(
        default=None,
        metadata={
            "name": "BearingCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_steps: None | int = field(
        default=None,
        metadata={
            "name": "NumberOfSteps",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    boarding_height: None | Decimal = field(
        default=None,
        metadata={
            "name": "BoardingHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    equipment_length: None | Decimal = field(
        default=None,
        metadata={
            "name": "EquipmentLength",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    equipment_width: None | Decimal = field(
        default=None,
        metadata={
            "name": "EquipmentWidth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    gap_to_platform: None | Decimal = field(
        default=None,
        metadata={
            "name": "GapToPlatform",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    width_of_access_area: None | Decimal = field(
        default=None,
        metadata={
            "name": "WidthOfAccessArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    height_of_access_area: None | Decimal = field(
        default=None,
        metadata={
            "name": "HeightOfAccessArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    automatic_doors: None | bool = field(
        default=None,
        metadata={
            "name": "AutomaticDoors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    suitable_for: Sequence[MobilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "SuitableFor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    assistance_needed: None | AssistanceNeededEnumeration = field(
        default=None,
        metadata={
            "name": "AssistanceNeeded",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    assisted_boarding_location: None | AssistedBoardingLocationEnumeration = (
        field(
            default=None,
            metadata={
                "name": "AssistedBoardingLocation",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    guide_dogs_allowed: None | bool = field(
        default=None,
        metadata={
            "name": "GuideDogsAllowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
