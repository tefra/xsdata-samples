from dataclasses import dataclass, field
from typing import List, Optional
from .all_modes_enumeration import AllModesEnumeration
from .alternative_texts_rel_structure import VersionedChildStructure
from .multilingual_string import MultilingualString
from .operational_context_ref import OperationalContextRef
from .time_demand_type_ref import TimeDemandTypeRef
from .timeband_ref import TimebandRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyTimingVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "JourneyTiming_VersionedChildStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_demand_type_ref_or_timeband_ref: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TimeDemandTypeRef",
                    "type": TimeDemandTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimebandRef",
                    "type": TimebandRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 2,
        }
    )
    vehicle_mode: Optional[AllModesEnumeration] = field(
        default=None,
        metadata={
            "name": "VehicleMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operational_context_ref: Optional[OperationalContextRef] = field(
        default=None,
        metadata={
            "name": "OperationalContextRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
