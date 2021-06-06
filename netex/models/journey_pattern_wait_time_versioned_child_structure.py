from dataclasses import dataclass, field
from typing import List, Optional
from .dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from .journey_pattern_ref import JourneyPatternRef
from .journey_wait_time_versioned_child_structure import JourneyWaitTimeVersionedChildStructure
from .service_journey_pattern_ref import ServiceJourneyPatternRef
from .service_pattern_ref import ServicePatternRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyPatternWaitTimeVersionedChildStructure(JourneyWaitTimeVersionedChildStructure):
    class Meta:
        name = "JourneyPatternWaitTime_VersionedChildStructure"

    service_journey_pattern_ref: List[ServiceJourneyPatternRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    service_pattern_ref: List[ServicePatternRef] = field(
        default_factory=list,
        metadata={
            "name": "ServicePatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    dead_run_journey_pattern_ref: List[DeadRunJourneyPatternRef] = field(
        default_factory=list,
        metadata={
            "name": "DeadRunJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    journey_pattern_ref: Optional[JourneyPatternRef] = field(
        default=None,
        metadata={
            "name": "JourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
