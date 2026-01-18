from __future__ import annotations

from dataclasses import dataclass

from .zone_projection_ref_structure import ZoneProjectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TopographicProjectionRefStructure(ZoneProjectionRefStructure):
    pass
