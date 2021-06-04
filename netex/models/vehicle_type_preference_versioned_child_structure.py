from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.day_type_ref import DayTypeRef
from netex.models.fare_day_type_ref import FareDayTypeRef
from netex.models.journey_timing_versioned_child_structure import JourneyTimingVersionedChildStructure
from netex.models.vehicle_type_preference_ref import VehicleTypePreferenceRef

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
    fare_day_type_ref: List[FareDayTypeRef] = field(
        default_factory=list,
        metadata={
            "name": "FareDayTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
        }
    )
    day_type_ref: Optional[DayTypeRef] = field(
        default=None,
        metadata={
            "name": "DayTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_type_preference_ref: Optional[VehicleTypePreferenceRef] = field(
        default=None,
        metadata={
            "name": "VehicleTypePreferenceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
