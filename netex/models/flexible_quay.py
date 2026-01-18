from __future__ import annotations

from dataclasses import dataclass

from .flexible_quay_version_structure import FlexibleQuayVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleQuay(FlexibleQuayVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
