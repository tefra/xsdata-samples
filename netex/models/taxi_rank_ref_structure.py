from dataclasses import dataclass

from .stop_place_ref_structure import StopPlaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TaxiRankRefStructure(StopPlaceRefStructure):
    pass
