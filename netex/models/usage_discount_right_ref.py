from __future__ import annotations

from dataclasses import dataclass

from .usage_discount_right_ref_structure import UsageDiscountRightRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UsageDiscountRightRef(UsageDiscountRightRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
