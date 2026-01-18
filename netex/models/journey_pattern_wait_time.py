from __future__ import annotations

from dataclasses import dataclass

from .journey_pattern_wait_time_versioned_child_structure import (
    JourneyPatternWaitTimeVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyPatternWaitTime(JourneyPatternWaitTimeVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
