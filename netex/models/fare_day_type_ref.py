from __future__ import annotations

from dataclasses import dataclass

from .fare_day_type_ref_structure import FareDayTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareDayTypeRef(FareDayTypeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
