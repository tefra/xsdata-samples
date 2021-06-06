from dataclasses import dataclass, field
from typing import List
from .commercial_profile_eligibility import CommercialProfileEligibility
from .containment_aggregation_structure import ContainmentAggregationStructure
from .customer_eligibility_1 import CustomerEligibility1
from .customer_eligibility_2 import CustomerEligibility2
from .residential_qualification_eligibility import ResidentialQualificationEligibility
from .user_profile_eligibility import UserProfileEligibility

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerEligibilitiesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "customerEligibilities_RelStructure"

    residential_qualification_eligibility: List[ResidentialQualificationEligibility] = field(
        default_factory=list,
        metadata={
            "name": "ResidentialQualificationEligibility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    commercial_profile_eligibility: List[CommercialProfileEligibility] = field(
        default_factory=list,
        metadata={
            "name": "CommercialProfileEligibility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    user_profile_eligibility: List[UserProfileEligibility] = field(
        default_factory=list,
        metadata={
            "name": "UserProfileEligibility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    customer_eligibility: List[CustomerEligibility1] = field(
        default_factory=list,
        metadata={
            "name": "CustomerEligibility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_customer_eligibility: List[CustomerEligibility2] = field(
        default_factory=list,
        metadata={
            "name": "CustomerEligibility_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
