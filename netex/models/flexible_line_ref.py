from __future__ import annotations

from dataclasses import dataclass

from .flexible_line_ref_structure import FlexibleLineRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FlexibleLineRef(FlexibleLineRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
