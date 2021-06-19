from dataclasses import dataclass, field
from typing import List, Optional
from .day_type_ref import DayTypeRef
from .fare_day_type_ref import FareDayTypeRef
from .journey_timing_versioned_child_structure import JourneyTimingVersionedChildStructure
from .vehicle_type_preference_ref import VehicleTypePreferenceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleTypePreferenceVersionedChildStructure(JourneyTimingVersionedChildStructure):
    class Meta:
        name = "VehicleTypePreference_VersionedChildStructure"

    rank: Optional[int] = field(
        default=None,
        metadata={
            "name": "Rank",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_day_type_ref_or_day_type_ref_or_vehicle_type_preference_ref: List[object] = field(
        default_factory=list,
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
                {
                    "name": "VehicleTypePreferenceRef",
                    "type": VehicleTypePreferenceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 4,
        }
    )
