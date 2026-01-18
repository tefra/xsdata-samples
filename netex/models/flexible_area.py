from __future__ import annotations

from dataclasses import dataclass

from .flexible_area_version_structure import FlexibleAreaVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleArea(FlexibleAreaVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
