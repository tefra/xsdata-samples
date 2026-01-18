from __future__ import annotations

from dataclasses import dataclass

from .road_link_ref_structure import RoadLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoadLinkRef(RoadLinkRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
