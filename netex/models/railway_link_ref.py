from __future__ import annotations

from dataclasses import dataclass

from .railway_link_ref_structure import RailwayLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RailwayLinkRef(RailwayLinkRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
