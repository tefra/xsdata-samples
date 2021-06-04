from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.dated_service_journey import DatedServiceJourney
from netex.models.service_journey_2 import ServiceJourney2
from netex.models.special_service import SpecialService
from netex.models.template_service_journey import TemplateServiceJourney

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
    service_journey: List[ServiceJourney2] = field(
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
