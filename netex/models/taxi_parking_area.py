from dataclasses import dataclass

from .taxi_parking_area_version_structure import (
    TaxiParkingAreaVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TaxiParkingArea(TaxiParkingAreaVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
