from dataclasses import dataclass, field
from typing import List
from .cancelling_ref import CancellingRef
from .charging_policy_ref import ChargingPolicyRef
from .commercial_profile_ref import CommercialProfileRef
from .companion_profile_ref import CompanionProfileRef
from .eligibility_change_policy_ref import EligibilityChangePolicyRef
from .entitlement_given_ref import EntitlementGivenRef
from .entitlement_required_ref import EntitlementRequiredRef
from .exchanging_ref import ExchangingRef
from .frequency_of_use_ref import FrequencyOfUseRef
from .group_ticket_ref import GroupTicketRef
from .interchanging_ref import InterchangingRef
from .luggage_allowance_ref import LuggageAllowanceRef
from .minimum_stay_ref import MinimumStayRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .penalty_policy_ref import PenaltyPolicyRef
from .profile_parameter_ref import ProfileParameterRef
from .purchase_window_ref import PurchaseWindowRef
from .refunding_ref import RefundingRef
from .replacing_ref import ReplacingRef
from .reselling_ref import ResellingRef
from .reserving_ref import ReservingRef
from .round_trip_ref import RoundTripRef
from .routing_ref import RoutingRef
from .sales_offer_package_entitlement_given_ref import SalesOfferPackageEntitlementGivenRef
from .sales_offer_package_entitlement_required_ref import SalesOfferPackageEntitlementRequiredRef
from .step_limit_ref import StepLimitRef
from .subscribing_ref import SubscribingRef
from .suspending_ref import SuspendingRef
from .transferability_ref import TransferabilityRef
from .usage_validity_period_ref import UsageValidityPeriodRef
from .user_profile_ref import UserProfileRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UsageParameterRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "usageParameterRefs_RelStructure"

    sales_offer_package_entitlement_given_ref: List[SalesOfferPackageEntitlementGivenRef] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackageEntitlementGivenRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_offer_package_entitlement_required_ref: List[SalesOfferPackageEntitlementRequiredRef] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackageEntitlementRequiredRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    minimum_stay_ref: List[MinimumStayRef] = field(
        default_factory=list,
        metadata={
            "name": "MinimumStayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    interchanging_ref: List[InterchangingRef] = field(
        default_factory=list,
        metadata={
            "name": "InterchangingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    frequency_of_use_ref: List[FrequencyOfUseRef] = field(
        default_factory=list,
        metadata={
            "name": "FrequencyOfUseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    suspending_ref: List[SuspendingRef] = field(
        default_factory=list,
        metadata={
            "name": "SuspendingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    usage_validity_period_ref: List[UsageValidityPeriodRef] = field(
        default_factory=list,
        metadata={
            "name": "UsageValidityPeriodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    step_limit_ref: List[StepLimitRef] = field(
        default_factory=list,
        metadata={
            "name": "StepLimitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    routing_ref: List[RoutingRef] = field(
        default_factory=list,
        metadata={
            "name": "RoutingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    round_trip_ref: List[RoundTripRef] = field(
        default_factory=list,
        metadata={
            "name": "RoundTripRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    luggage_allowance_ref: List[LuggageAllowanceRef] = field(
        default_factory=list,
        metadata={
            "name": "LuggageAllowanceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entitlement_given_ref: List[EntitlementGivenRef] = field(
        default_factory=list,
        metadata={
            "name": "EntitlementGivenRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entitlement_required_ref: List[EntitlementRequiredRef] = field(
        default_factory=list,
        metadata={
            "name": "EntitlementRequiredRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    eligibility_change_policy_ref: List[EligibilityChangePolicyRef] = field(
        default_factory=list,
        metadata={
            "name": "EligibilityChangePolicyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_ticket_ref: List[GroupTicketRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupTicketRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    commercial_profile_ref: List[CommercialProfileRef] = field(
        default_factory=list,
        metadata={
            "name": "CommercialProfileRef",
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
        }
    )
    user_profile_ref: List[UserProfileRef] = field(
        default_factory=list,
        metadata={
            "name": "UserProfileRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    profile_parameter_ref: List[ProfileParameterRef] = field(
        default_factory=list,
        metadata={
            "name": "ProfileParameterRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    subscribing_ref: List[SubscribingRef] = field(
        default_factory=list,
        metadata={
            "name": "SubscribingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    penalty_policy_ref: List[PenaltyPolicyRef] = field(
        default_factory=list,
        metadata={
            "name": "PenaltyPolicyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    charging_policy_ref: List[ChargingPolicyRef] = field(
        default_factory=list,
        metadata={
            "name": "ChargingPolicyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transferability_ref: List[TransferabilityRef] = field(
        default_factory=list,
        metadata={
            "name": "TransferabilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    replacing_ref: List[ReplacingRef] = field(
        default_factory=list,
        metadata={
            "name": "ReplacingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    refunding_ref: List[RefundingRef] = field(
        default_factory=list,
        metadata={
            "name": "RefundingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    exchanging_ref: List[ExchangingRef] = field(
        default_factory=list,
        metadata={
            "name": "ExchangingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    reselling_ref: List[ResellingRef] = field(
        default_factory=list,
        metadata={
            "name": "ResellingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    cancelling_ref: List[CancellingRef] = field(
        default_factory=list,
        metadata={
            "name": "CancellingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    reserving_ref: List[ReservingRef] = field(
        default_factory=list,
        metadata={
            "name": "ReservingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    purchase_window_ref: List[PurchaseWindowRef] = field(
        default_factory=list,
        metadata={
            "name": "PurchaseWindowRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
