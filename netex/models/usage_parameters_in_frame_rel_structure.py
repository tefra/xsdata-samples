from dataclasses import dataclass, field
from typing import List
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
from .replacing import Replacing
from .reselling import Reselling
from .reserving import Reserving
from .round_trip import RoundTrip
from .routing import Routing
from .sales_offer_package_entitlement_given import SalesOfferPackageEntitlementGiven
from .sales_offer_package_entitlement_required import SalesOfferPackageEntitlementRequired
from .step_limit import StepLimit
from .subscribing import Subscribing
from .suspending import Suspending
from .transferability import Transferability
from .usage_parameter_1 import UsageParameter1
from .usage_parameter_2 import UsageParameter2
from .usage_validity_period import UsageValidityPeriod
from .user_profile import UserProfile

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UsageParametersInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "usageParametersInFrame_RelStructure"

    sales_offer_package_entitlement_required: List[SalesOfferPackageEntitlementRequired] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackageEntitlementRequired",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    sales_offer_package_entitlement_given: List[SalesOfferPackageEntitlementGiven] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackageEntitlementGiven",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    minimum_stay: List[MinimumStay] = field(
        default_factory=list,
        metadata={
            "name": "MinimumStay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    interchanging: List[Interchanging] = field(
        default_factory=list,
        metadata={
            "name": "Interchanging",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    suspending: List[Suspending] = field(
        default_factory=list,
        metadata={
            "name": "Suspending",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    usage_validity_period: List[UsageValidityPeriod] = field(
        default_factory=list,
        metadata={
            "name": "UsageValidityPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    frequency_of_use: List[FrequencyOfUse] = field(
        default_factory=list,
        metadata={
            "name": "FrequencyOfUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    step_limit: List[StepLimit] = field(
        default_factory=list,
        metadata={
            "name": "StepLimit",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    routing: List[Routing] = field(
        default_factory=list,
        metadata={
            "name": "Routing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    round_trip: List[RoundTrip] = field(
        default_factory=list,
        metadata={
            "name": "RoundTrip",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    luggage_allowance: List[LuggageAllowance] = field(
        default_factory=list,
        metadata={
            "name": "LuggageAllowance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    entitlement_required: List[EntitlementRequired] = field(
        default_factory=list,
        metadata={
            "name": "EntitlementRequired",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    entitlement_given: List[EntitlementGiven] = field(
        default_factory=list,
        metadata={
            "name": "EntitlementGiven",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    eligibility_change_policy: List[EligibilityChangePolicy] = field(
        default_factory=list,
        metadata={
            "name": "EligibilityChangePolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    companion_profile: List[CompanionProfile] = field(
        default_factory=list,
        metadata={
            "name": "CompanionProfile",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    group_ticket: List[GroupTicket] = field(
        default_factory=list,
        metadata={
            "name": "GroupTicket",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    commercial_profile: List[CommercialProfile] = field(
        default_factory=list,
        metadata={
            "name": "CommercialProfile",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    user_profile: List[UserProfile] = field(
        default_factory=list,
        metadata={
            "name": "UserProfile",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    subscribing: List[Subscribing] = field(
        default_factory=list,
        metadata={
            "name": "Subscribing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    penalty_policy: List[PenaltyPolicy] = field(
        default_factory=list,
        metadata={
            "name": "PenaltyPolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    charging_policy: List[ChargingPolicy] = field(
        default_factory=list,
        metadata={
            "name": "ChargingPolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    cancelling: List[Cancelling] = field(
        default_factory=list,
        metadata={
            "name": "Cancelling",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    reserving: List[Reserving] = field(
        default_factory=list,
        metadata={
            "name": "Reserving",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    purchase_window: List[PurchaseWindow] = field(
        default_factory=list,
        metadata={
            "name": "PurchaseWindow",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    transferability: List[Transferability] = field(
        default_factory=list,
        metadata={
            "name": "Transferability",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    replacing: List[Replacing] = field(
        default_factory=list,
        metadata={
            "name": "Replacing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    refunding: List[Refunding] = field(
        default_factory=list,
        metadata={
            "name": "Refunding",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    exchanging: List[Exchanging] = field(
        default_factory=list,
        metadata={
            "name": "Exchanging",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    reselling: List[Reselling] = field(
        default_factory=list,
        metadata={
            "name": "Reselling",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    usage_parameter: List[UsageParameter1] = field(
        default_factory=list,
        metadata={
            "name": "UsageParameter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_usage_parameter: List[UsageParameter2] = field(
        default_factory=list,
        metadata={
            "name": "UsageParameter_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )