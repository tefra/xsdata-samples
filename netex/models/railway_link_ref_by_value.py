from __future__ import annotations

from dataclasses import dataclass

from .railway_link_ref_by_value_structure import RailwayLinkRefByValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RailwayLinkRefByValue(RailwayLinkRefByValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
