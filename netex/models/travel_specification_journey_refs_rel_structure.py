from dataclasses import dataclass, field
from typing import List
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.models.service_journey_ref import ServiceJourneyRef
from netex.models.template_service_journey_ref import TemplateServiceJourneyRef
from netex.models.train_number_ref import TrainNumberRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TravelSpecificationJourneyRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "travelSpecificationJourneyRefs_RelStructure"

    template_service_journey_ref: List[TemplateServiceJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "TemplateServiceJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_journey_ref: List[ServiceJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_number_ref: List[TrainNumberRef] = field(
        default_factory=list,
        metadata={
            "name": "TrainNumberRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
