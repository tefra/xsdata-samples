from dataclasses import dataclass, field
from typing import List
from .commercial_profile_eligibility_ref import CommercialProfileEligibilityRef
from .customer_eligibility_ref import CustomerEligibilityRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .residential_qualification_eligibility_ref import ResidentialQualificationEligibilityRef
from .user_profile_eligibility_ref import UserProfileEligibilityRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerEligibilityRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "customerEligibilityRefs_RelStructure"

    residential_qualification_eligibility_ref: List[ResidentialQualificationEligibilityRef] = field(
        default_factory=list,
        metadata={
            "name": "ResidentialQualificationEligibilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    commercial_profile_eligibility_ref: List[CommercialProfileEligibilityRef] = field(
        default_factory=list,
        metadata={
            "name": "CommercialProfileEligibilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    user_profile_eligibility_ref: List[UserProfileEligibilityRef] = field(
        default_factory=list,
        metadata={
            "name": "UserProfileEligibilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    customer_eligibility_ref: List[CustomerEligibilityRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerEligibilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
