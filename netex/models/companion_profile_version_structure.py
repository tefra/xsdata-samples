from dataclasses import dataclass, field
from typing import Optional, Union

from .companion_profile_ref import CompanionProfileRef
from .companion_relationship_enumeration import (
    CompanionRelationshipEnumeration,
)
from .discount_basis_enumeration import DiscountBasisEnumeration
from .usage_parameter_ref_structure import UsageParameterRefStructure
from .usage_parameter_version_structure import UsageParameterVersionStructure
from .user_profile_ref import UserProfileRef
from .vehicle_pooler_profile_ref import VehiclePoolerProfileRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CompanionProfileVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "CompanionProfile_VersionStructure"

    parent_ref: UsageParameterRefStructure | None = field(
        default=None,
        metadata={
            "name": "ParentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    user_profile_ref: VehiclePoolerProfileRef | CompanionProfileRef | UserProfileRef | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehiclePoolerProfileRef",
                    "type": VehiclePoolerProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
            ),
        },
    )
    companion_relationship_type: CompanionRelationshipEnumeration | None = (
        field(
            default=None,
            metadata={
                "name": "CompanionRelationshipType",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    minimum_number_of_persons: int | None = field(
        default=None,
        metadata={
            "name": "MinimumNumberOfPersons",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_number_of_persons: int | None = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfPersons",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    discount_basis: DiscountBasisEnumeration | None = field(
        default=None,
        metadata={
            "name": "DiscountBasis",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
