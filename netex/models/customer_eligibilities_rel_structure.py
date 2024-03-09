from dataclasses import dataclass, field
from typing import List, Union

from .commercial_profile_eligibility import CommercialProfileEligibility
from .containment_aggregation_structure import ContainmentAggregationStructure
from .residential_qualification_eligibility import (
    ResidentialQualificationEligibility,
)
from .user_profile_eligibility import UserProfileEligibility

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerEligibilitiesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "customerEligibilities_RelStructure"

    customer_eligibility: List[
        Union[
            ResidentialQualificationEligibility,
            CommercialProfileEligibility,
            UserProfileEligibility,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ResidentialQualificationEligibility",
                    "type": ResidentialQualificationEligibility,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommercialProfileEligibility",
                    "type": CommercialProfileEligibility,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UserProfileEligibility",
                    "type": UserProfileEligibility,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
