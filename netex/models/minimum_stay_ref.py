from __future__ import annotations

from dataclasses import dataclass

from .minimum_stay_ref_structure import MinimumStayRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MinimumStayRef(MinimumStayRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
