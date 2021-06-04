from dataclasses import dataclass, field
from typing import List
from netex.models.amount_of_price_unit_product_ref import AmountOfPriceUnitProductRef
from netex.models.cancelling_ref import CancellingRef
from netex.models.capped_discount_right_ref import CappedDiscountRightRef
from netex.models.capping_rule_ref import CappingRuleRef
from netex.models.charging_policy_ref import ChargingPolicyRef
from netex.models.commercial_profile_ref import CommercialProfileRef
from netex.models.companion_profile_ref import CompanionProfileRef
from netex.models.controllable_element_ref import ControllableElementRef
from netex.models.customer_purchase_package_element_ref import CustomerPurchasePackageElementRef
from netex.models.customer_purchase_package_ref import CustomerPurchasePackageRef
from netex.models.distance_matrix_element_inverse_ref import DistanceMatrixElementInverseRef
from netex.models.distance_matrix_element_ref import DistanceMatrixElementRef
from netex.models.eligibility_change_policy_ref import EligibilityChangePolicyRef
from netex.models.entitlement_given_ref import EntitlementGivenRef
from netex.models.entitlement_product_ref import EntitlementProductRef
from netex.models.entitlement_required_ref import EntitlementRequiredRef
from netex.models.exchanging_ref import ExchangingRef
from netex.models.fare_demand_factor_ref import FareDemandFactorRef
from netex.models.fare_interval_ref import FareIntervalRef
from netex.models.fare_product_ref import FareProductRef
from netex.models.fare_quota_factor_ref import FareQuotaFactorRef
from netex.models.fare_structure_element_ref import FareStructureElementRef
from netex.models.fare_structure_factor_ref import FareStructureFactorRef
from netex.models.frequency_of_use_ref import FrequencyOfUseRef
from netex.models.fulfilment_method_ref import FulfilmentMethodRef
from netex.models.geographical_interval_ref import GeographicalIntervalRef
from netex.models.geographical_structure_factor_ref import GeographicalStructureFactorRef
from netex.models.group_ticket_ref import GroupTicketRef
from netex.models.interchanging_ref import InterchangingRef
from netex.models.luggage_allowance_ref import LuggageAllowanceRef
from netex.models.minimum_stay_ref import MinimumStayRef
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.models.parking_charge_band_ref import ParkingChargeBandRef
from netex.models.penalty_policy_ref import PenaltyPolicyRef
from netex.models.preassigned_fare_product_ref import PreassignedFareProductRef
from netex.models.priceable_object_ref import PriceableObjectRef
from netex.models.profile_parameter_ref import ProfileParameterRef
from netex.models.purchase_window_ref import PurchaseWindowRef
from netex.models.quality_structure_factor_ref import QualityStructureFactorRef
from netex.models.refunding_ref import RefundingRef
from netex.models.replacing_ref import ReplacingRef
from netex.models.reselling_ref import ResellingRef
from netex.models.reserving_ref import ReservingRef
from netex.models.round_trip_ref import RoundTripRef
from netex.models.routing_ref import RoutingRef
from netex.models.sale_discount_right_ref import SaleDiscountRightRef
from netex.models.sales_offer_package_element_ref import SalesOfferPackageElementRef
from netex.models.sales_offer_package_entitlement_given_ref import SalesOfferPackageEntitlementGivenRef
from netex.models.sales_offer_package_entitlement_required_ref import SalesOfferPackageEntitlementRequiredRef
from netex.models.sales_offer_package_ref import SalesOfferPackageRef
from netex.models.series_constraint_ref import SeriesConstraintRef
from netex.models.service_access_right_ref import ServiceAccessRightRef
from netex.models.step_limit_ref import StepLimitRef
from netex.models.subscribing_ref import SubscribingRef
from netex.models.supplement_product_ref import SupplementProductRef
from netex.models.suspending_ref import SuspendingRef
from netex.models.third_party_product_ref import ThirdPartyProductRef
from netex.models.time_interval_ref import TimeIntervalRef
from netex.models.time_structure_factor_ref import TimeStructureFactorRef
from netex.models.transferability_ref import TransferabilityRef
from netex.models.usage_discount_right_ref import UsageDiscountRightRef
from netex.models.usage_parameter_ref import UsageParameterRef
from netex.models.usage_validity_period_ref import UsageValidityPeriodRef
from netex.models.user_profile_ref import UserProfileRef
from netex.models.validable_element_ref import ValidableElementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PriceableObjectRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "priceableObjectRefs_RelStructure"

    customer_purchase_package_element_ref: List[CustomerPurchasePackageElementRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerPurchasePackageElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    customer_purchase_package_ref: List[CustomerPurchasePackageRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerPurchasePackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    controllable_element_ref: List[ControllableElementRef] = field(
        default_factory=list,
        metadata={
            "name": "ControllableElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    validable_element_ref: List[ValidableElementRef] = field(
        default_factory=list,
        metadata={
            "name": "ValidableElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    sales_offer_package_entitlement_given_ref: List[SalesOfferPackageEntitlementGivenRef] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackageEntitlementGivenRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    sales_offer_package_entitlement_required_ref: List[SalesOfferPackageEntitlementRequiredRef] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackageEntitlementRequiredRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    minimum_stay_ref: List[MinimumStayRef] = field(
        default_factory=list,
        metadata={
            "name": "MinimumStayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    interchanging_ref: List[InterchangingRef] = field(
        default_factory=list,
        metadata={
            "name": "InterchangingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    frequency_of_use_ref: List[FrequencyOfUseRef] = field(
        default_factory=list,
        metadata={
            "name": "FrequencyOfUseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    suspending_ref: List[SuspendingRef] = field(
        default_factory=list,
        metadata={
            "name": "SuspendingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    usage_validity_period_ref: List[UsageValidityPeriodRef] = field(
        default_factory=list,
        metadata={
            "name": "UsageValidityPeriodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    step_limit_ref: List[StepLimitRef] = field(
        default_factory=list,
        metadata={
            "name": "StepLimitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    routing_ref: List[RoutingRef] = field(
        default_factory=list,
        metadata={
            "name": "RoutingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    round_trip_ref: List[RoundTripRef] = field(
        default_factory=list,
        metadata={
            "name": "RoundTripRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    luggage_allowance_ref: List[LuggageAllowanceRef] = field(
        default_factory=list,
        metadata={
            "name": "LuggageAllowanceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    entitlement_given_ref: List[EntitlementGivenRef] = field(
        default_factory=list,
        metadata={
            "name": "EntitlementGivenRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    entitlement_required_ref: List[EntitlementRequiredRef] = field(
        default_factory=list,
        metadata={
            "name": "EntitlementRequiredRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    eligibility_change_policy_ref: List[EligibilityChangePolicyRef] = field(
        default_factory=list,
        metadata={
            "name": "EligibilityChangePolicyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    group_ticket_ref: List[GroupTicketRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupTicketRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    commercial_profile_ref: List[CommercialProfileRef] = field(
        default_factory=list,
        metadata={
            "name": "CommercialProfileRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    companion_profile_ref: List[CompanionProfileRef] = field(
        default_factory=list,
        metadata={
            "name": "CompanionProfileRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    user_profile_ref: List[UserProfileRef] = field(
        default_factory=list,
        metadata={
            "name": "UserProfileRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    profile_parameter_ref: List[ProfileParameterRef] = field(
        default_factory=list,
        metadata={
            "name": "ProfileParameterRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    subscribing_ref: List[SubscribingRef] = field(
        default_factory=list,
        metadata={
            "name": "SubscribingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    penalty_policy_ref: List[PenaltyPolicyRef] = field(
        default_factory=list,
        metadata={
            "name": "PenaltyPolicyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    charging_policy_ref: List[ChargingPolicyRef] = field(
        default_factory=list,
        metadata={
            "name": "ChargingPolicyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    transferability_ref: List[TransferabilityRef] = field(
        default_factory=list,
        metadata={
            "name": "TransferabilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    replacing_ref: List[ReplacingRef] = field(
        default_factory=list,
        metadata={
            "name": "ReplacingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    refunding_ref: List[RefundingRef] = field(
        default_factory=list,
        metadata={
            "name": "RefundingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    exchanging_ref: List[ExchangingRef] = field(
        default_factory=list,
        metadata={
            "name": "ExchangingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    reselling_ref: List[ResellingRef] = field(
        default_factory=list,
        metadata={
            "name": "ResellingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    cancelling_ref: List[CancellingRef] = field(
        default_factory=list,
        metadata={
            "name": "CancellingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    reserving_ref: List[ReservingRef] = field(
        default_factory=list,
        metadata={
            "name": "ReservingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    purchase_window_ref: List[PurchaseWindowRef] = field(
        default_factory=list,
        metadata={
            "name": "PurchaseWindowRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    usage_parameter_ref: List[UsageParameterRef] = field(
        default_factory=list,
        metadata={
            "name": "UsageParameterRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    sales_offer_package_element_ref: List[SalesOfferPackageElementRef] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackageElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    sales_offer_package_ref: List[SalesOfferPackageRef] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    distance_matrix_element_inverse_ref: List[DistanceMatrixElementInverseRef] = field(
        default_factory=list,
        metadata={
            "name": "DistanceMatrixElementInverseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    distance_matrix_element_ref: List[DistanceMatrixElementRef] = field(
        default_factory=list,
        metadata={
            "name": "DistanceMatrixElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_structure_element_ref: List[FareStructureElementRef] = field(
        default_factory=list,
        metadata={
            "name": "FareStructureElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fulfilment_method_ref: List[FulfilmentMethodRef] = field(
        default_factory=list,
        metadata={
            "name": "FulfilmentMethodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    series_constraint_ref: List[SeriesConstraintRef] = field(
        default_factory=list,
        metadata={
            "name": "SeriesConstraintRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    capping_rule_ref: List[CappingRuleRef] = field(
        default_factory=list,
        metadata={
            "name": "CappingRuleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    entitlement_product_ref: List[EntitlementProductRef] = field(
        default_factory=list,
        metadata={
            "name": "EntitlementProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    supplement_product_ref: List[SupplementProductRef] = field(
        default_factory=list,
        metadata={
            "name": "SupplementProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    preassigned_fare_product_ref: List[PreassignedFareProductRef] = field(
        default_factory=list,
        metadata={
            "name": "PreassignedFareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    amount_of_price_unit_product_ref: List[AmountOfPriceUnitProductRef] = field(
        default_factory=list,
        metadata={
            "name": "AmountOfPriceUnitProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    usage_discount_right_ref: List[UsageDiscountRightRef] = field(
        default_factory=list,
        metadata={
            "name": "UsageDiscountRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    third_party_product_ref: List[ThirdPartyProductRef] = field(
        default_factory=list,
        metadata={
            "name": "ThirdPartyProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    capped_discount_right_ref: List[CappedDiscountRightRef] = field(
        default_factory=list,
        metadata={
            "name": "CappedDiscountRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    sale_discount_right_ref: List[SaleDiscountRightRef] = field(
        default_factory=list,
        metadata={
            "name": "SaleDiscountRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_product_ref: List[FareProductRef] = field(
        default_factory=list,
        metadata={
            "name": "FareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    service_access_right_ref: List[ServiceAccessRightRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceAccessRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    time_interval_ref: List[TimeIntervalRef] = field(
        default_factory=list,
        metadata={
            "name": "TimeIntervalRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    geographical_interval_ref: List[GeographicalIntervalRef] = field(
        default_factory=list,
        metadata={
            "name": "GeographicalIntervalRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_interval_ref: List[FareIntervalRef] = field(
        default_factory=list,
        metadata={
            "name": "FareIntervalRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    parking_charge_band_ref: List[ParkingChargeBandRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingChargeBandRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    time_structure_factor_ref: List[TimeStructureFactorRef] = field(
        default_factory=list,
        metadata={
            "name": "TimeStructureFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_quota_factor_ref: List[FareQuotaFactorRef] = field(
        default_factory=list,
        metadata={
            "name": "FareQuotaFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_demand_factor_ref: List[FareDemandFactorRef] = field(
        default_factory=list,
        metadata={
            "name": "FareDemandFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    quality_structure_factor_ref: List[QualityStructureFactorRef] = field(
        default_factory=list,
        metadata={
            "name": "QualityStructureFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    geographical_structure_factor_ref: List[GeographicalStructureFactorRef] = field(
        default_factory=list,
        metadata={
            "name": "GeographicalStructureFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_structure_factor_ref: List[FareStructureFactorRef] = field(
        default_factory=list,
        metadata={
            "name": "FareStructureFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    priceable_object_ref: List[PriceableObjectRef] = field(
        default_factory=list,
        metadata={
            "name": "PriceableObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
