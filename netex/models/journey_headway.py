from dataclasses import dataclass
from .journey_headway_versioned_child_structure import JourneyHeadwayVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyHeadway(JourneyHeadwayVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
