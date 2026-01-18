from __future__ import annotations

from dataclasses import dataclass

from .journey_timing_ref_structure import JourneyTimingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyTimingRef(JourneyTimingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
