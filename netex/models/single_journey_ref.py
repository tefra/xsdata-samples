from __future__ import annotations

from dataclasses import dataclass

from .single_journey_ref_structure import SingleJourneyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SingleJourneyRef(SingleJourneyRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
