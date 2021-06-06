from dataclasses import dataclass, field
from typing import List
from .service_journey_interchange import ServiceJourneyInterchange
from .service_journey_interchange_ref import ServiceJourneyInterchangeRef
from .service_journey_interchange_view import ServiceJourneyInterchangeView
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceJourneyInterchangesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "serviceJourneyInterchanges_RelStructure"

    service_journey_interchange_ref: List[ServiceJourneyInterchangeRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourneyInterchangeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_journey_interchange: List[ServiceJourneyInterchange] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourneyInterchange",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_journey_interchange_view: List[ServiceJourneyInterchangeView] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourneyInterchangeView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
