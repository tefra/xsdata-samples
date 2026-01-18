from __future__ import annotations

from dataclasses import dataclass

from .lost_property_service_ref_structure import (
    LostPropertyServiceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LostPropertyServiceRef(LostPropertyServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
