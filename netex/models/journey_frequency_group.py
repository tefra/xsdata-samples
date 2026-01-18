from __future__ import annotations

from dataclasses import dataclass

from .journey_frequency_group_version_structure import (
    JourneyFrequencyGroupVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyFrequencyGroup(JourneyFrequencyGroupVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
