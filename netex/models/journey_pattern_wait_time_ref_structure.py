from __future__ import annotations

from dataclasses import dataclass

from .journey_timing_ref_structure import JourneyTimingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyPatternWaitTimeRefStructure(JourneyTimingRefStructure):
    pass
