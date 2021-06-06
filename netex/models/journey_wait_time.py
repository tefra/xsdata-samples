from dataclasses import dataclass
from .journey_wait_time_versioned_child_structure import JourneyWaitTimeVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyWaitTime(JourneyWaitTimeVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
