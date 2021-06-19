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

    driver_trip_time_ref_or_driver_trip_time: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DriverTripTimeRef",
                    "type": DriverTripTimeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DriverTripTime",
                    "type": DriverTripTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
