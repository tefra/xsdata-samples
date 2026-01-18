from __future__ import annotations

from dataclasses import dataclass

from .travel_agent_ref_structure import TravelAgentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TravelAgentRef(TravelAgentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
