from dataclasses import dataclass

from .driver_trip_ref_structure import DriverTripRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DriverTripRef(DriverTripRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
