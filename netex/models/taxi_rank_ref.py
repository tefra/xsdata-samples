from __future__ import annotations

from dataclasses import dataclass

from .taxi_rank_ref_structure import TaxiRankRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TaxiRankRef(TaxiRankRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
