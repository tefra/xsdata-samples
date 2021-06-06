from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .driver_trip_time import DriverTripTime
from .driver_trip_time_ref import DriverTripTimeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DriverTripTimesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "driverTripTimes_RelStructure"

    driver_trip_time_ref: List[DriverTripTimeRef] = field(
        default_factory=list,
        metadata={
            "name": "DriverTripTimeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    driver_trip_time: List[DriverTripTime] = field(
        default_factory=list,
        metadata={
            "name": "DriverTripTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
