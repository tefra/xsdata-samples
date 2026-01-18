from __future__ import annotations

from dataclasses import dataclass

from .journey_part_version_structure import JourneyPartVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyPart(JourneyPartVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
