from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from .derived_view_structure import DerivedViewStructure
from .passenger_capacity import PassengerCapacity

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassengerCarryingPassengerCarryingViewStructure(DerivedViewStructure):
    class Meta:
        name = "PassengerCarryingPassengerCarrying_ViewStructure"

    passenger_capacity: PassengerCapacity | None = field(
        default=None,
        metadata={
            "name": "PassengerCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    low_floor: bool | None = field(
        default=None,
        metadata={
            "name": "LowFloor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_lift_or_ramp: bool | None = field(
        default=None,
        metadata={
            "name": "HasLiftOrRamp",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_hoist: bool | None = field(
        default=None,
        metadata={
            "name": "HasHoist",
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
    gap_to_platform: Decimal | None = field(
        default=None,
        metadata={
            "name": "GapToPlatform",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
