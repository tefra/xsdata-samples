from __future__ import annotations

from dataclasses import dataclass

from .topographic_projection_version_structure import (
    TopographicProjectionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TopographicProjection(TopographicProjectionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
