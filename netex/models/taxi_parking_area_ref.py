from dataclasses import dataclass

from .taxi_parking_area_ref_structure import TaxiParkingAreaRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TaxiParkingAreaRef(TaxiParkingAreaRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
