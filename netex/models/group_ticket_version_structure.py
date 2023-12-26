from dataclasses import dataclass, field
from typing import Optional
from .companion_profiles_rel_structure import CompanionProfilesRelStructure
from .group_booking_enumeration import GroupBookingEnumeration
from .group_check_in_enumeration import GroupCheckInEnumeration
from .group_size_changes_enumeration import GroupSizeChangesEnumeration
from .group_ticketing_enumeration import GroupTicketingEnumeration
from .per_basis_enumeration import PerBasisEnumeration
from .type_of_concession_ref import TypeOfConcessionRef
from .usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupTicketVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "GroupTicket_VersionStructure"

    type_of_concession_ref: Optional[TypeOfConcessionRef] = field(
        default=None,
        metadata={
            "name": "TypeOfConcessionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_number_of_persons: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinimumNumberOfPersons",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_number_of_persons: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfPersons",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_number_of_card_holders: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinimumNumberOfCardHolders",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    companion_profiles: Optional[CompanionProfilesRelStructure] = field(
        default=None,
        metadata={
            "name": "companionProfiles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    pricing_basis: Optional[PerBasisEnumeration] = field(
        default=None,
        metadata={
            "name": "PricingBasis",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_persons_free: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumPersonsFree",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_persons_discounted: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumPersonsDiscounted",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    discount_only_for_first_person: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DiscountOnlyForFirstPerson",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    one_for_npersons: Optional[int] = field(
        default=None,
        metadata={
            "name": "OneForNPersons",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    group_size_changes: Optional[GroupSizeChangesEnumeration] = field(
        default=None,
        metadata={
            "name": "GroupSizeChanges",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    ticketing: Optional[GroupTicketingEnumeration] = field(
        default=None,
        metadata={
            "name": "Ticketing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    joint_check_in: Optional[GroupCheckInEnumeration] = field(
        default=None,
        metadata={
            "name": "JointCheckIn",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    group_booking_facility: Optional[GroupBookingEnumeration] = field(
        default=None,
        metadata={
            "name": "GroupBookingFacility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
