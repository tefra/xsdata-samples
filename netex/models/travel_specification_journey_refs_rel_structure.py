from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .service_journey_ref import ServiceJourneyRef
from .single_journey_ref import SingleJourneyRef
from .template_service_journey_ref import TemplateServiceJourneyRef
from .train_number_ref import TrainNumberRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TravelSpecificationJourneyRefsRelStructure(
    OneToManyRelationshipStructure
):
    class Meta:
        name = "travelSpecificationJourneyRefs_RelStructure"

    choice: Iterable[
        Union[
            TemplateServiceJourneyRef,
            ServiceJourneyRef,
            SingleJourneyRef,
            TrainNumberRef,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TemplateServiceJourneyRef",
                    "type": TemplateServiceJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyRef",
                    "type": ServiceJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SingleJourneyRef",
                    "type": SingleJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainNumberRef",
                    "type": TrainNumberRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
