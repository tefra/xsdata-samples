from dataclasses import dataclass

from .taxi_rank_ref_structure import TaxiRankRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TaxiRankRef(TaxiRankRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
