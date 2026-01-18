from __future__ import annotations

from collections.abc import Iterable
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


@dataclass
class AccessVehicleEquipmentVersionStructure(
    ActualVehicleEquipmentVersionStructure
):
    class Meta:
        name = "AccessVehicleEquipment_VersionStructure"

    low_floor: bool | None = field(
        default=None,
        metadata={
            "name": "LowFloor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    high_floor: bool | None = field(
        default=None,
        metadata={
            "name": "HighFloor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    hoist: bool | None = field(
        default=None,
        metadata={
            "name": "Hoist",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    ramp: bool | None = field(
        default=None,
        metadata={
            "name": "Ramp",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    bearing_capacity: Decimal | None = field(
        default=None,
        metadata={
            "name": "BearingCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_steps: int | None = field(
        default=None,
        metadata={
            "name": "NumberOfSteps",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    boarding_height: Decimal | None = field(
        default=None,
        metadata={
            "name": "BoardingHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    equipment_length: Decimal | None = field(
        default=None,
        metadata={
            "name": "EquipmentLength",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    equipment_width: Decimal | None = field(
        default=None,
        metadata={
            "name": "EquipmentWidth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    gap_to_platform: Decimal | None = field(
        default=None,
        metadata={
            "name": "GapToPlatform",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    width_of_access_area: Decimal | None = field(
        default=None,
        metadata={
            "name": "WidthOfAccessArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    height_of_access_area: Decimal | None = field(
        default=None,
        metadata={
            "name": "HeightOfAccessArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    automatic_doors: bool | None = field(
        default=None,
        metadata={
            "name": "AutomaticDoors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    suitable_for: Iterable[MobilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "SuitableFor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    assistance_needed: AssistanceNeededEnumeration | None = field(
        default=None,
        metadata={
            "name": "AssistanceNeeded",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    assisted_boarding_location: AssistedBoardingLocationEnumeration | None = (
        field(
            default=None,
            metadata={
                "name": "AssistedBoardingLocation",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    guide_dogs_allowed: bool | None = field(
        default=None,
        metadata={
            "name": "GuideDogsAllowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
