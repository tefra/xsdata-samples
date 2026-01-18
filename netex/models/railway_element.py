from __future__ import annotations

from dataclasses import dataclass

from .railway_element_version_structure import RailwayElementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RailwayElement(RailwayElementVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
