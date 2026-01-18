from __future__ import annotations

from dataclasses import dataclass

from .month_validity_offset_versioned_structure import (
    MonthValidityOffsetVersionedStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MonthValidityOffset(MonthValidityOffsetVersionedStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
