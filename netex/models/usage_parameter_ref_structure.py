from __future__ import annotations

from dataclasses import dataclass

from .priceable_object_ref_structure import PriceableObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UsageParameterRefStructure(PriceableObjectRefStructure):
    pass
