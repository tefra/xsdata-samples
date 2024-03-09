from dataclasses import dataclass

from .dead_run_journey_pattern_ref_structure import (
    DeadRunJourneyPatternRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DeadRunJourneyPatternRef(DeadRunJourneyPatternRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
