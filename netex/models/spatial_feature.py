from __future__ import annotations

from dataclasses import dataclass

from .group_of_points_version_structure import GroupOfPointsVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SpatialFeature(GroupOfPointsVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
