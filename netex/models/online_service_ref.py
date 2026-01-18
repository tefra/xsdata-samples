from __future__ import annotations

from dataclasses import dataclass

from .online_service_ref_structure import OnlineServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OnlineServiceRef(OnlineServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
