from __future__ import annotations

from dataclasses import dataclass

from .relief_opportunity_version_structure import (
    ReliefOpportunityVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ReliefOpportunity(ReliefOpportunityVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
