from __future__ import annotations

from dataclasses import dataclass

from .point_projection_version_structure import PointProjectionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointProjection(PointProjectionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
