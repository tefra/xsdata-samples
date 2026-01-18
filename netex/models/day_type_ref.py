from __future__ import annotations

from dataclasses import dataclass

from .day_type_ref_structure import DayTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DayTypeRef(DayTypeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
