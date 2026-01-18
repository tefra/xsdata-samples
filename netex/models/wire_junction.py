from __future__ import annotations

from dataclasses import dataclass

from .wire_junction_version_structure import WireJunctionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WireJunction(WireJunctionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
