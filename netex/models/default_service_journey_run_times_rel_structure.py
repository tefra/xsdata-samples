from dataclasses import dataclass, field
from typing import List

from .default_service_journey_run_time import DefaultServiceJourneyRunTime
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DefaultServiceJourneyRunTimesRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "defaultServiceJourneyRunTimes_RelStructure"

    default_service_journey_run_time: List[DefaultServiceJourneyRunTime] = (
        field(
            default_factory=list,
            metadata={
                "name": "DefaultServiceJourneyRunTime",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            },
        )
    )
