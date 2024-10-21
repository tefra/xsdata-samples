from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .parking_bay_condition import ParkingBayCondition
from .rental_availability import RentalAvailability

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingLogEntriesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "parkingLogEntriesInFrame_RelStructure"

    parking_log_entry: Iterable[
        Union[ParkingBayCondition, RentalAvailability]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ParkingBayCondition",
                    "type": ParkingBayCondition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RentalAvailability",
                    "type": RentalAvailability,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
