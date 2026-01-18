from __future__ import annotations

from dataclasses import dataclass

from .mobility_service_ref_structure import MobilityServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MobilityServiceRef(MobilityServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
