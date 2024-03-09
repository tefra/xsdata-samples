from dataclasses import dataclass

from .parking_price_ref_structure import ParkingPriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingPriceRef(ParkingPriceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
