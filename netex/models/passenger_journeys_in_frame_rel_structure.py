from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .dated_service_journey import DatedServiceJourney
from .service_journey_1 import ServiceJourney1
from .special_service import SpecialService
from .template_service_journey import TemplateServiceJourney

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassengerJourneysInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "passengerJourneysInFrame_RelStructure"

    dated_service_journey: List[DatedServiceJourney] = field(
        default_factory=list,
        metadata={
            "name": "DatedServiceJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_journey: List[ServiceJourney1] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    special_service: List[SpecialService] = field(
        default_factory=list,
        metadata={
            "name": "SpecialService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    template_service_journey: List[TemplateServiceJourney] = field(
        default_factory=list,
        metadata={
            "name": "TemplateServiceJourney",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
