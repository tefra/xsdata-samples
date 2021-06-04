from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.companion_profile_ref import CompanionProfileRef
from netex.models.companion_relationship_enumeration import CompanionRelationshipEnumeration
from netex.models.discount_basis_enumeration import DiscountBasisEnumeration
from netex.models.usage_parameter_ref_structure import UsageParameterRefStructure
from netex.models.usage_parameter_version_structure import UsageParameterVersionStructure
from netex.models.user_profile_ref import UserProfileRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CompanionProfileVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "CompanionProfile_VersionStructure"

    parent_ref: Optional[UsageParameterRefStructure] = field(
        default=None,
        metadata={
            "name": "ParentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    companion_profile_ref: List[CompanionProfileRef] = field(
        default_factory=list,
        metadata={
            "name": "CompanionProfileRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
        }
    )
    user_profile_ref: Optional[UserProfileRef] = field(
        default=None,
        metadata={
            "name": "UserProfileRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    companion_relationship_type: Optional[CompanionRelationshipEnumeration] = field(
        default=None,
        metadata={
            "name": "CompanionRelationshipType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    minimum_number_of_persons: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinimumNumberOfPersons",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_number_of_persons: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfPersons",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    discount_basis: Optional[DiscountBasisEnumeration] = field(
        default=None,
        metadata={
            "name": "DiscountBasis",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
