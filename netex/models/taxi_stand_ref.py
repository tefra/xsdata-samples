from __future__ import annotations

from dataclasses import dataclass

from .taxi_stand_ref_structure import TaxiStandRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TaxiStandRef(TaxiStandRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
