from dataclasses import dataclass, field
from typing import List, Union
from .containment_aggregation_structure import ContainmentAggregationStructure
from .individual_traveller import IndividualTraveller
from .individual_traveller_ref import IndividualTravellerRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class IndividualTravellersRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "individualTravellers_RelStructure"

    individual_traveller_ref_or_individual_traveller: List[
        Union[IndividualTravellerRef, IndividualTraveller]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "IndividualTravellerRef",
                    "type": IndividualTravellerRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "IndividualTraveller",
                    "type": IndividualTraveller,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
