from dataclasses import dataclass, field
from typing import Optional
from netex.models.all_modes_enumeration import AllModesEnumeration
from netex.models.alternative_texts_rel_structure import VersionedChildStructure
from netex.models.multilingual_string import MultilingualString
from netex.models.operational_context_ref import OperationalContextRef
from netex.models.time_demand_type_ref import TimeDemandTypeRef
from netex.models.timeband_ref import TimebandRef

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
    time_demand_type_ref: Optional[TimeDemandTypeRef] = field(
        default=None,
        metadata={
            "name": "TimeDemandTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timeband_ref: Optional[TimebandRef] = field(
        default=None,
        metadata={
            "name": "TimebandRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
