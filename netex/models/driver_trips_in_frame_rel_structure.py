from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .driver_trip import DriverTrip

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DriverTripsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "driverTripsInFrame_RelStructure"

    driver_trip: Iterable[DriverTrip] = field(
        default_factory=list,
        metadata={
            "name": "DriverTrip",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
