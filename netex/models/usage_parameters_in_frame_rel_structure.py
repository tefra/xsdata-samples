from collections.abc import Iterable
from dataclasses import dataclass, field

from .additional_driver_option import AdditionalDriverOption
from .cancelling import Cancelling
from .charging_policy import ChargingPolicy
from .commercial_profile import CommercialProfile
from .companion_profile import CompanionProfile
from .eligibility_change_policy import EligibilityChangePolicy
from .entitlement_given import EntitlementGiven
from .entitlement_required import EntitlementRequired
from .exchanging import Exchanging
from .frame_containment_structure import FrameContainmentStructure
from .frequency_of_use import FrequencyOfUse
from .group_ticket import GroupTicket
from .interchanging import Interchanging
from .luggage_allowance import LuggageAllowance
from .minimum_stay import MinimumStay
from .penalty_policy import PenaltyPolicy
from .purchase_window import PurchaseWindow
from .refunding import Refunding
from .rental_option import RentalOption
from .rental_penalty_policy import RentalPenaltyPolicy
from .replacing import Replacing
from .reselling import Reselling
from .reserving import Reserving
from .round_trip import RoundTrip
from .routing import Routing
from .sales_offer_package_entitlement_given import (
    SalesOfferPackageEntitlementGiven,
)
from .sales_offer_package_entitlement_required import (
    SalesOfferPackageEntitlementRequired,
)
from .step_limit import StepLimit
from .subscribing import Subscribing
from .suspending import Suspending
from .transferability import Transferability
from .usage_validity_period import UsageValidityPeriod
from .user_profile import UserProfile
from .vehicle_pooler_profile import VehiclePoolerProfile

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UsageParametersInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "usageParametersInFrame_RelStructure"

    usage_parameter: Iterable[
        AdditionalDriverOption
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
