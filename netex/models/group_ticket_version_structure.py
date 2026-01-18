from __future__ import annotations

from dataclasses import dataclass, field

from .companion_profiles_rel_structure import CompanionProfilesRelStructure
from .group_booking_facility import GroupBookingFacility
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

    type_of_concession_ref: None | TypeOfConcessionRef = field(
        default=None,
        metadata={
            "name": "TypeOfConcessionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_number_of_persons: None | int = field(
        default=None,
        metadata={
            "name": "MinimumNumberOfPersons",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_number_of_persons: None | int = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfPersons",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_number_of_card_holders: None | int = field(
        default=None,
        metadata={
            "name": "MinimumNumberOfCardHolders",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    companion_profiles: None | CompanionProfilesRelStructure = field(
        default=None,
        metadata={
            "name": "companionProfiles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    pricing_basis: None | PerBasisEnumeration = field(
        default=None,
        metadata={
            "name": "PricingBasis",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_persons_free: None | int = field(
        default=None,
        metadata={
            "name": "MaximumPersonsFree",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_persons_discounted: None | int = field(
        default=None,
        metadata={
            "name": "MaximumPersonsDiscounted",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    discount_only_for_first_person: None | bool = field(
        default=None,
        metadata={
            "name": "DiscountOnlyForFirstPerson",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    one_for_npersons: None | int = field(
        default=None,
        metadata={
            "name": "OneForNPersons",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    group_size_changes: None | GroupSizeChangesEnumeration = field(
        default=None,
        metadata={
            "name": "GroupSizeChanges",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    ticketing: None | GroupTicketingEnumeration = field(
        default=None,
        metadata={
            "name": "Ticketing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    joint_check_in: None | GroupCheckInEnumeration = field(
        default=None,
        metadata={
            "name": "JointCheckIn",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    group_booking_facility: None | GroupBookingFacility = field(
        default=None,
        metadata={
            "name": "GroupBookingFacility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
