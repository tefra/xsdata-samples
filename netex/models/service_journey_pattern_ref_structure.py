from __future__ import annotations

from dataclasses import dataclass

from .journey_pattern_ref_structure import JourneyPatternRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceJourneyPatternRefStructure(JourneyPatternRefStructure):
    pass
