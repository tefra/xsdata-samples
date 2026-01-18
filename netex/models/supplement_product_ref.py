from __future__ import annotations

from dataclasses import dataclass

from .supplement_product_ref_structure import SupplementProductRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SupplementProductRef(SupplementProductRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
