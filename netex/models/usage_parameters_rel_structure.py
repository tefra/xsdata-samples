from collections.abc import Iterable
from dataclasses import dataclass, field

from .additional_driver_option import AdditionalDriverOption
from .additional_driver_option_ref import AdditionalDriverOptionRef
from .booking_policy_ref import BookingPolicyRef
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
from .rental_option import RentalOption
from .rental_option_ref import RentalOptionRef
from .rental_penalty_policy import RentalPenaltyPolicy
from .rental_penalty_policy_ref import RentalPenaltyPolicyRef
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
from .sales_offer_package_entitlement_given import (
    SalesOfferPackageEntitlementGiven,
)
from .sales_offer_package_entitlement_given_ref import (
    SalesOfferPackageEntitlementGivenRef,
)
from .sales_offer_package_entitlement_required import (
    SalesOfferPackageEntitlementRequired,
)
from .sales_offer_package_entitlement_required_ref import (
    SalesOfferPackageEntitlementRequiredRef,
)
from .step_limit import StepLimit
from .step_limit_ref import StepLimitRef
from .subscribing import Subscribing
from .subscribing_ref import SubscribingRef
from .suspending import Suspending
from .suspending_ref import SuspendingRef
from .transferability import Transferability
from .transferability_ref import TransferabilityRef
from .usage_validity_period import UsageValidityPeriod
from .usage_validity_period_ref import UsageValidityPeriodRef
from .user_profile import UserProfile
from .user_profile_ref import UserProfileRef
from .vehicle_pooler_profile import VehiclePoolerProfile
from .vehicle_pooler_profile_ref import VehiclePoolerProfileRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UsageParametersRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "usageParameters_RelStructure"

    choice: Iterable[
        AdditionalDriverOptionRef
        | RentalOptionRef
        | RentalPenaltyPolicyRef
        | SalesOfferPackageEntitlementGivenRef
        | SalesOfferPackageEntitlementRequiredRef
        | MinimumStayRef
        | InterchangingRef
        | FrequencyOfUseRef
        | SuspendingRef
        | UsageValidityPeriodRef
        | StepLimitRef
        | RoutingRef
        | RoundTripRef
        | LuggageAllowanceRef
        | EntitlementGivenRef
        | EntitlementRequiredRef
        | EligibilityChangePolicyRef
        | GroupTicketRef
        | CommercialProfileRef
        | VehiclePoolerProfileRef
        | CompanionProfileRef
        | UserProfileRef
        | ProfileParameterRef
        | SubscribingRef
        | PenaltyPolicyRef
        | ChargingPolicyRef
        | TransferabilityRef
        | ReplacingRef
        | RefundingRef
        | ExchangingRef
        | ResellingRef
        | CancellingRef
        | ReservingRef
        | BookingPolicyRef
        | PurchaseWindowRef
        | AdditionalDriverOption
        | RentalOption
        | RentalPenaltyPolicy
        | VehiclePoolerProfile
        | SalesOfferPackageEntitlementRequired
        | SalesOfferPackageEntitlementGiven
        | MinimumStay
        | Interchanging
        | Suspending
        | UsageValidityPeriod
        | FrequencyOfUse
        | StepLimit
        | Routing
        | RoundTrip
        | LuggageAllowance
        | EntitlementRequired
        | EntitlementGiven
        | EligibilityChangePolicy
        | CompanionProfile
        | GroupTicket
        | CommercialProfile
        | UserProfile
        | Subscribing
        | PenaltyPolicy
        | ChargingPolicy
        | Cancelling
        | Reserving
        | PurchaseWindow
        | Transferability
        | Replacing
        | Refunding
        | Exchanging
        | Reselling
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AdditionalDriverOptionRef",
                    "type": AdditionalDriverOptionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RentalOptionRef",
                    "type": RentalOptionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RentalPenaltyPolicyRef",
                    "type": RentalPenaltyPolicyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageEntitlementGivenRef",
                    "type": SalesOfferPackageEntitlementGivenRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageEntitlementRequiredRef",
                    "type": SalesOfferPackageEntitlementRequiredRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MinimumStayRef",
                    "type": MinimumStayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "InterchangingRef",
                    "type": InterchangingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FrequencyOfUseRef",
                    "type": FrequencyOfUseRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SuspendingRef",
                    "type": SuspendingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageValidityPeriodRef",
                    "type": UsageValidityPeriodRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StepLimitRef",
                    "type": StepLimitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoutingRef",
                    "type": RoutingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoundTripRef",
                    "type": RoundTripRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LuggageAllowanceRef",
                    "type": LuggageAllowanceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntitlementGivenRef",
                    "type": EntitlementGivenRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntitlementRequiredRef",
                    "type": EntitlementRequiredRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EligibilityChangePolicyRef",
                    "type": EligibilityChangePolicyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupTicketRef",
                    "type": GroupTicketRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommercialProfileRef",
                    "type": CommercialProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "ProfileParameterRef",
                    "type": ProfileParameterRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SubscribingRef",
                    "type": SubscribingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PenaltyPolicyRef",
                    "type": PenaltyPolicyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChargingPolicyRef",
                    "type": ChargingPolicyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransferabilityRef",
                    "type": TransferabilityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReplacingRef",
                    "type": ReplacingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RefundingRef",
                    "type": RefundingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ExchangingRef",
                    "type": ExchangingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ResellingRef",
                    "type": ResellingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CancellingRef",
                    "type": CancellingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReservingRef",
                    "type": ReservingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BookingPolicyRef",
                    "type": BookingPolicyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PurchaseWindowRef",
                    "type": PurchaseWindowRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AdditionalDriverOption",
                    "type": AdditionalDriverOption,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RentalOption",
                    "type": RentalOption,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RentalPenaltyPolicy",
                    "type": RentalPenaltyPolicy,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePoolerProfile",
                    "type": VehiclePoolerProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageEntitlementRequired",
                    "type": SalesOfferPackageEntitlementRequired,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageEntitlementGiven",
                    "type": SalesOfferPackageEntitlementGiven,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MinimumStay",
                    "type": MinimumStay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Interchanging",
                    "type": Interchanging,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Suspending",
                    "type": Suspending,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageValidityPeriod",
                    "type": UsageValidityPeriod,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FrequencyOfUse",
                    "type": FrequencyOfUse,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StepLimit",
                    "type": StepLimit,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Routing",
                    "type": Routing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoundTrip",
                    "type": RoundTrip,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LuggageAllowance",
                    "type": LuggageAllowance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntitlementRequired",
                    "type": EntitlementRequired,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntitlementGiven",
                    "type": EntitlementGiven,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EligibilityChangePolicy",
                    "type": EligibilityChangePolicy,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompanionProfile",
                    "type": CompanionProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupTicket",
                    "type": GroupTicket,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommercialProfile",
                    "type": CommercialProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UserProfile",
                    "type": UserProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Subscribing",
                    "type": Subscribing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PenaltyPolicy",
                    "type": PenaltyPolicy,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChargingPolicy",
                    "type": ChargingPolicy,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Cancelling",
                    "type": Cancelling,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Reserving",
                    "type": Reserving,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PurchaseWindow",
                    "type": PurchaseWindow,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Transferability",
                    "type": Transferability,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Replacing",
                    "type": Replacing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Refunding",
                    "type": Refunding,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Exchanging",
                    "type": Exchanging,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Reselling",
                    "type": Reselling,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
