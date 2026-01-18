from __future__ import annotations

from dataclasses import dataclass

from .timing_pattern_version_structure import TimingPatternVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimingPattern(TimingPatternVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
