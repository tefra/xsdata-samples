from __future__ import annotations

from dataclasses import dataclass

from .special_service_ref_structure import SpecialServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SpecialServiceRef(SpecialServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
