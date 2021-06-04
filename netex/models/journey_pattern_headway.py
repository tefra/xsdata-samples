from dataclasses import dataclass
from netex.models.journey_pattern_headway_versioned_child_structure import JourneyPatternHeadwayVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyPatternHeadway(JourneyPatternHeadwayVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
