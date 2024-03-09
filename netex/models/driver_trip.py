from dataclasses import dataclass

from .driver_trip_version_structure import DriverTripVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DriverTrip(DriverTripVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
