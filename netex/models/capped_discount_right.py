from __future__ import annotations

from dataclasses import dataclass

from .capped_discount_right_version_structure import (
    CappedDiscountRightVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CappedDiscountRight(CappedDiscountRightVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
