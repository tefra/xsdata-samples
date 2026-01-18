from dataclasses import dataclass, field
from typing import Optional, Union

from .day_type_ref import DayTypeRef
from .fare_day_type_ref import FareDayTypeRef
from .journey_timing_versioned_child_structure import (
    JourneyTimingVersionedChildStructure,
)
from .vehicle_type_preference_ref import VehicleTypePreferenceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleTypePreferenceVersionedChildStructure(
    JourneyTimingVersionedChildStructure
):
    class Meta:
        name = "VehicleTypePreference_VersionedChildStructure"

    rank: int | None = field(
        default=None,
        metadata={
            "name": "Rank",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    day_type_ref: FareDayTypeRef | DayTypeRef | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareDayTypeRef",
                    "type": FareDayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayTypeRef",
                    "type": DayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    vehicle_type_preference_ref: VehicleTypePreferenceRef | None = field(
        default=None,
        metadata={
            "name": "VehicleTypePreferenceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
