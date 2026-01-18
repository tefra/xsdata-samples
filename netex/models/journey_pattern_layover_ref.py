from __future__ import annotations

from dataclasses import dataclass

from .journey_pattern_layover_ref_structure import (
    JourneyPatternLayoverRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyPatternLayoverRef(JourneyPatternLayoverRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
