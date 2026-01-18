from __future__ import annotations

from dataclasses import dataclass

from .flexible_quay_ref_structure import FlexibleQuayRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FlexibleQuayRef(FlexibleQuayRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
