from __future__ import annotations

from dataclasses import dataclass

from .road_element_version_structure import RoadElementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RoadElement(RoadElementVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
