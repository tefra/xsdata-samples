from dataclasses import dataclass, field
from typing import List
from .dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from .journey_pattern_ref import JourneyPatternRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .service_journey_pattern_ref import ServiceJourneyPatternRef
from .service_pattern_ref import ServicePatternRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyPatternRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "journeyPatternRefs_RelStructure"

    service_journey_pattern_ref: List[ServiceJourneyPatternRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    service_pattern_ref: List[ServicePatternRef] = field(
        default_factory=list,
        metadata={
            "name": "ServicePatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    dead_run_journey_pattern_ref: List[DeadRunJourneyPatternRef] = field(
        default_factory=list,
        metadata={
            "name": "DeadRunJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    journey_pattern_ref: List[JourneyPatternRef] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
