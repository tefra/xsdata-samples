from dataclasses import dataclass, field
from typing import List, Optional
from .alternative_texts_rel_structure import DataManagedObjectStructure
from .dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from .dead_run_ref import DeadRunRef
from .journey_pattern_ref import JourneyPatternRef
from .multilingual_string import MultilingualString
from .service_journey_pattern_ref import ServiceJourneyPatternRef
from .service_pattern_ref import ServicePatternRef
from .time_demand_profile_members_rel_structure import TimeDemandProfileMembersRelStructure
from .time_demand_type_ref import TimeDemandTypeRef
from .timeband_ref import TimebandRef
from .vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimeDemandProfileVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "TimeDemandProfile_VersionStructure"

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
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceJourneyPatternRef",
                    "type": ServiceJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicePatternRef",
                    "type": ServicePatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRunJourneyPatternRef",
                    "type": DeadRunJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternRef",
                    "type": JourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRunRef",
                    "type": DeadRunRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleJourneyRef",
                    "type": VehicleJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "members",
                    "type": TimeDemandProfileMembersRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 8,
        }
    )
