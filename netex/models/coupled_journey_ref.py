from __future__ import annotations

from dataclasses import dataclass

from .coupled_journey_ref_structure import CoupledJourneyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CoupledJourneyRef(CoupledJourneyRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
