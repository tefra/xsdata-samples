from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .commercial_profile_eligibility_ref import CommercialProfileEligibilityRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .residential_qualification_eligibility_ref import (
    ResidentialQualificationEligibilityRef,
)
from .user_profile_eligibility_ref import UserProfileEligibilityRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerEligibilityRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "customerEligibilityRefs_RelStructure"

    customer_eligibility_ref: Iterable[
        ResidentialQualificationEligibilityRef
        | CommercialProfileEligibilityRef
        | UserProfileEligibilityRef
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ResidentialQualificationEligibilityRef",
                    "type": ResidentialQualificationEligibilityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommercialProfileEligibilityRef",
                    "type": CommercialProfileEligibilityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UserProfileEligibilityRef",
                    "type": UserProfileEligibilityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
