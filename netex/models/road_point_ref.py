from __future__ import annotations

from dataclasses import dataclass

from .road_point_ref_structure import RoadPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoadPointRef(RoadPointRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
