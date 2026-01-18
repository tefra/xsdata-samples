from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from .derived_view_structure import DerivedViewStructure
from .passenger_capacity import PassengerCapacity

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerCarryingPassengerCarryingViewStructure(DerivedViewStructure):
    class Meta:
        name = "PassengerCarryingPassengerCarrying_ViewStructure"

    passenger_capacity: None | PassengerCapacity = field(
        default=None,
        metadata={
            "name": "PassengerCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    low_floor: None | bool = field(
        default=None,
        metadata={
            "name": "LowFloor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_lift_or_ramp: None | bool = field(
        default=None,
        metadata={
            "name": "HasLiftOrRamp",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_hoist: None | bool = field(
        default=None,
        metadata={
            "name": "HasHoist",
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
    gap_to_platform: None | Decimal = field(
        default=None,
        metadata={
            "name": "GapToPlatform",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
