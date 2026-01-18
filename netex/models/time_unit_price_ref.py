from __future__ import annotations

from dataclasses import dataclass

from .time_unit_price_ref_structure import TimeUnitPriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimeUnitPriceRef(TimeUnitPriceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
