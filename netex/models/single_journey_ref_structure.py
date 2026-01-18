from __future__ import annotations

from dataclasses import dataclass

from .journey_ref_structure import JourneyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SingleJourneyRefStructure(JourneyRefStructure):
    pass
