from __future__ import annotations

from dataclasses import dataclass

from .point_on_link_ref_structure_2 import PointOnLinkRefStructure2

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOnLinkRefStructure1(PointOnLinkRefStructure2):
    class Meta:
        name = "PointOnLinkRefStructure"
