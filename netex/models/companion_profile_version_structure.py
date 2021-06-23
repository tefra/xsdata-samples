from dataclasses import dataclass, field
from typing import Optional
from .companion_profile_ref import CompanionProfileRef
from .companion_relationship_enumeration import CompanionRelationshipEnumeration
from .discount_basis_enumeration import DiscountBasisEnumeration
from .usage_parameter_ref_structure import UsageParameterRefStructure
from .usage_parameter_version_structure import UsageParameterVersionStructure
from .user_profile_ref import UserProfileRef

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
    companion_profile_ref: Optional[CompanionProfileRef] = field(
        default=None,
        metadata={
            "name": "CompanionProfileRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
