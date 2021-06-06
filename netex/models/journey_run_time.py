from dataclasses import dataclass
from .journey_run_time_versioned_child_structure import JourneyRunTimeVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyRunTime(JourneyRunTimeVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
