from dataclasses import dataclass, field
from typing import List
from .cancelling import Cancelling
from .cancelling_ref import CancellingRef
from .charging_policy import ChargingPolicy
from .charging_policy_ref import ChargingPolicyRef
from .commercial_profile import CommercialProfile
from .commercial_profile_ref import CommercialProfileRef
from .companion_profile import CompanionProfile
from .companion_profile_ref import CompanionProfileRef
from .eligibility_change_policy import EligibilityChangePolicy
from .eligibility_change_policy_ref import EligibilityChangePolicyRef
from .entitlement_given import EntitlementGiven
from .entitlement_given_ref import EntitlementGivenRef
from .entitlement_required import EntitlementRequired
from .entitlement_required_ref import EntitlementRequiredRef
from .exchanging import Exchanging
from .exchanging_ref import ExchangingRef
from .frequency_of_use import FrequencyOfUse
from .frequency_of_use_ref import FrequencyOfUseRef
from .group_ticket import GroupTicket
from .group_ticket_ref import GroupTicketRef
from .interchanging import Interchanging
from .interchanging_ref import InterchangingRef
from .luggage_allowance import LuggageAllowance
from .luggage_allowance_ref import LuggageAllowanceRef
from .minimum_stay import MinimumStay
from .minimum_stay_ref import MinimumStayRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .penalty_policy import PenaltyPolicy
from .penalty_policy_ref import PenaltyPolicyRef
from .profile_parameter_ref import ProfileParameterRef
from .purchase_window import PurchaseWindow
from .purchase_window_ref import PurchaseWindowRef
from .refunding import Refunding
from .refunding_ref import RefundingRef
from .replacing import Replacing
from .replacing_ref import ReplacingRef
from .reselling import Reselling
from .reselling_ref import ResellingRef
from .reserving import Reserving
from .reserving_ref import ReservingRef
from .round_trip import RoundTrip
from .round_trip_ref import RoundTripRef
from .routing import Routing
from .routing_ref import RoutingRef
from .sales_offer_package_entitlement_given import SalesOfferPackageEntitlementGiven
from .sales_offer_package_entitlement_given_ref import SalesOfferPackageEntitlementGivenRef
from .sales_offer_package_entitlement_required import SalesOfferPackageEntitlementRequired
from .sales_offer_package_entitlement_required_ref import SalesOfferPackageEntitlementRequiredRef
from .step_limit import StepLimit
from .step_limit_ref import StepLimitRef
from .subscribing import Subscribing
from .subscribing_ref import SubscribingRef
from .suspending import Suspending
from .suspending_ref import SuspendingRef
from .transferability import Transferability
from .transferability_ref import TransferabilityRef
from .usage_parameter_1 import UsageParameter1
from .usage_parameter_2 import UsageParameter2
from .usage_parameter_ref import UsageParameterRef
from .usage_validity_period import UsageValidityPeriod
from .usage_validity_period_ref import UsageValidityPeriodRef
from .user_profile import UserProfile
from .user_profile_ref import UserProfileRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UsageParametersRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "usageParameters_RelStructure"

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
    usage_parameter_ref: List[UsageParameterRef] = field(
        default_factory=list,
        metadata={
            "name": "UsageParameterRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_offer_package_entitlement_required: List[SalesOfferPackageEntitlementRequired] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackageEntitlementRequired",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_offer_package_entitlement_given: List[SalesOfferPackageEntitlementGiven] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackageEntitlementGiven",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    minimum_stay: List[MinimumStay] = field(
        default_factory=list,
        metadata={
            "name": "MinimumStay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    interchanging: List[Interchanging] = field(
        default_factory=list,
        metadata={
            "name": "Interchanging",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    suspending: List[Suspending] = field(
        default_factory=list,
        metadata={
            "name": "Suspending",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    usage_validity_period: List[UsageValidityPeriod] = field(
        default_factory=list,
        metadata={
            "name": "UsageValidityPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    frequency_of_use: List[FrequencyOfUse] = field(
        default_factory=list,
        metadata={
            "name": "FrequencyOfUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    step_limit: List[StepLimit] = field(
        default_factory=list,
        metadata={
            "name": "StepLimit",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    routing: List[Routing] = field(
        default_factory=list,
        metadata={
            "name": "Routing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    round_trip: List[RoundTrip] = field(
        default_factory=list,
        metadata={
            "name": "RoundTrip",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    luggage_allowance: List[LuggageAllowance] = field(
        default_factory=list,
        metadata={
            "name": "LuggageAllowance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entitlement_required: List[EntitlementRequired] = field(
        default_factory=list,
        metadata={
            "name": "EntitlementRequired",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entitlement_given: List[EntitlementGiven] = field(
        default_factory=list,
        metadata={
            "name": "EntitlementGiven",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    eligibility_change_policy: List[EligibilityChangePolicy] = field(
        default_factory=list,
        metadata={
            "name": "EligibilityChangePolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    companion_profile: List[CompanionProfile] = field(
        default_factory=list,
        metadata={
            "name": "CompanionProfile",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_ticket: List[GroupTicket] = field(
        default_factory=list,
        metadata={
            "name": "GroupTicket",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    commercial_profile: List[CommercialProfile] = field(
        default_factory=list,
        metadata={
            "name": "CommercialProfile",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    user_profile: List[UserProfile] = field(
        default_factory=list,
        metadata={
            "name": "UserProfile",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    subscribing: List[Subscribing] = field(
        default_factory=list,
        metadata={
            "name": "Subscribing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    penalty_policy: List[PenaltyPolicy] = field(
        default_factory=list,
        metadata={
            "name": "PenaltyPolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    charging_policy: List[ChargingPolicy] = field(
        default_factory=list,
        metadata={
            "name": "ChargingPolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    cancelling: List[Cancelling] = field(
        default_factory=list,
        metadata={
            "name": "Cancelling",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    reserving: List[Reserving] = field(
        default_factory=list,
        metadata={
            "name": "Reserving",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    purchase_window: List[PurchaseWindow] = field(
        default_factory=list,
        metadata={
            "name": "PurchaseWindow",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transferability: List[Transferability] = field(
        default_factory=list,
        metadata={
            "name": "Transferability",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    replacing: List[Replacing] = field(
        default_factory=list,
        metadata={
            "name": "Replacing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    refunding: List[Refunding] = field(
        default_factory=list,
        metadata={
            "name": "Refunding",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    exchanging: List[Exchanging] = field(
        default_factory=list,
        metadata={
            "name": "Exchanging",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    reselling: List[Reselling] = field(
        default_factory=list,
        metadata={
            "name": "Reselling",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    usage_parameter: List[UsageParameter1] = field(
        default_factory=list,
        metadata={
            "name": "UsageParameter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_usage_parameter: List[UsageParameter2] = field(
        default_factory=list,
        metadata={
            "name": "UsageParameter_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
