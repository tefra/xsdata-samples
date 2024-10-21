from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .service_journey_interchange import ServiceJourneyInterchange
from .service_journey_interchange_ref import ServiceJourneyInterchangeRef
from .service_journey_interchange_view import ServiceJourneyInterchangeView
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceJourneyInterchangesRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "serviceJourneyInterchanges_RelStructure"

    service_journey_interchange_ref_or_service_journey_interchange_or_service_journey_interchange_view: Iterable[
        Union[
            ServiceJourneyInterchangeRef,
            ServiceJourneyInterchange,
            ServiceJourneyInterchangeView,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceJourneyInterchangeRef",
                    "type": ServiceJourneyInterchangeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyInterchange",
                    "type": ServiceJourneyInterchange,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyInterchangeView",
                    "type": ServiceJourneyInterchangeView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
