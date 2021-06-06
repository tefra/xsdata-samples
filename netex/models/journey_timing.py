from dataclasses import dataclass
from .journey_timing_versioned_child_structure import JourneyTimingVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyTiming(JourneyTimingVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
