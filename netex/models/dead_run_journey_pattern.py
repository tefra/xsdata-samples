from __future__ import annotations

from dataclasses import dataclass

from .dead_run_journey_pattern_version_structure import (
    DeadRunJourneyPatternVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeadRunJourneyPattern(DeadRunJourneyPatternVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
