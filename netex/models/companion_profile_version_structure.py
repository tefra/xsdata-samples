from dataclasses import dataclass, field
from typing import List, Optional
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
    choice_1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CompanionProfileRef",
                    "type": CompanionProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UserProfileRef",
                    "type": UserProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompanionRelationshipType",
                    "type": CompanionRelationshipEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MinimumNumberOfPersons",
                    "type": int,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MaximumNumberOfPersons",
                    "type": int,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DiscountBasis",
                    "type": DiscountBasisEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 2,
        }
    )
