from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .parking_bay_condition import ParkingBayCondition
from .parking_bay_condition_ref import ParkingBayConditionRef
from .rental_availability import RentalAvailability
from .rental_availability_ref import RentalAvailabilityRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingLogEntriesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "parkingLogEntries_RelStructure"

    choice: Iterable[
        Union[
            ParkingBayConditionRef,
            RentalAvailabilityRef,
            ParkingBayCondition,
            RentalAvailability,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ParkingBayConditionRef",
                    "type": ParkingBayConditionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RentalAvailabilityRef",
                    "type": RentalAvailabilityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
