from __future__ import annotations

from dataclasses import dataclass

from .journey_layover_structure import JourneyLayoverStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyLayover(JourneyLayoverStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
