from __future__ import annotations

from dataclasses import dataclass

from .relief_opportunity_ref_structure import ReliefOpportunityRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ReliefOpportunityRef(ReliefOpportunityRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
