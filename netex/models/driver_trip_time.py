from dataclasses import dataclass
from netex.models.driver_trip_time_version_structure import DriverTripTimeVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DriverTripTime(DriverTripTimeVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
