from collections.abc import Iterable
from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlPeriod

from .companion_profiles_rel_structure import CompanionProfilesRelStructure
from .discount_basis_enumeration import DiscountBasisEnumeration
from .gender_limitation import GenderLimitation
from .proof_of_identity_enumeration import ProofOfIdentityEnumeration
from .residential_qualifications_rel_structure import (
    ResidentialQualificationsRelStructure,
)
from .type_of_concession_ref import TypeOfConcessionRef
from .types_of_proof_refs_rel_structure import TypesOfProofRefsRelStructure
from .usage_parameter_version_structure import UsageParameterVersionStructure
from .user_profile_ref_structure import UserProfileRefStructure
from .user_type_enumeration import UserTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UserProfileVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "UserProfile_VersionStructure"

    base_user_profile_ref: UserProfileRefStructure | None = field(
        default=None,
        metadata={
            "name": "BaseUserProfileRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_concession_ref: TypeOfConcessionRef | None = field(
        default=None,
        metadata={
            "name": "TypeOfConcessionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    user_type: UserTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "UserType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_age: int | None = field(
        default=None,
        metadata={
            "name": "MinimumAge",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_age: int | None = field(
        default=None,
        metadata={
            "name": "MaximumAge",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    month_day_on_which_age_applies: XmlPeriod | None = field(
        default=None,
        metadata={
            "name": "MonthDayOnWhichAgeApplies",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_height: Decimal | None = field(
        default=None,
        metadata={
            "name": "MinimumHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_height: Decimal | None = field(
        default=None,
        metadata={
            "name": "MaximumHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    local_resident: bool | None = field(
        default=None,
        metadata={
            "name": "LocalResident",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    resides: ResidentialQualificationsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    gender_limitation: GenderLimitation | None = field(
        default=None,
        metadata={
            "name": "GenderLimitation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    proof_required: Iterable[ProofOfIdentityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ProofRequired",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    types_of_proof_required_ref: TypesOfProofRefsRelStructure | None = (
        field(
            default=None,
            metadata={
                "name": "typesOfProofRequiredRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    discount_basis: DiscountBasisEnumeration | None = field(
        default=None,
        metadata={
            "name": "DiscountBasis",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    companion_profiles: CompanionProfilesRelStructure | None = field(
        default=None,
        metadata={
            "name": "companionProfiles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
