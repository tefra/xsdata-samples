from dataclasses import dataclass, field
from typing import List, Optional, Type, Union
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration
from .alternative_names_rel_structure import AlternativeNamesRelStructure
from .alternative_texts_rel_structure import (
    DataManagedObjectStructure,
    VersionedChildStructure,
)
from .amount_of_price_unit_product_ref import AmountOfPriceUnitProductRef
from .authority_ref import AuthorityRef
from .cancelling_ref import CancellingRef
from .capped_discount_right_ref import CappedDiscountRightRef
from .capping_rule_price import CappingRulePrice
from .capping_rule_price_ref import CappingRulePriceRef
from .capping_rule_ref import CappingRuleRef
from .cell_ref import CellRef
from .charging_policy_ref import ChargingPolicyRef
from .class_of_use_ref import ClassOfUseRef
from .commercial_profile_ref import CommercialProfileRef
from .companion_profile_ref import CompanionProfileRef
from .compound_train_ref import CompoundTrainRef
from .controllable_element_price import ControllableElementPrice
from .controllable_element_price_ref import ControllableElementPriceRef
from .controllable_element_ref import ControllableElementRef
from .customer_purchase_package_element_ref import (
    CustomerPurchasePackageElementRef,
)
from .customer_purchase_package_price import CustomerPurchasePackagePrice
from .customer_purchase_package_price_ref import (
    CustomerPurchasePackagePriceRef,
)
from .customer_purchase_package_ref import CustomerPurchasePackageRef
from .discounting_rule_ref import DiscountingRuleRef
from .distance_matrix_element_inverse_ref import (
    DistanceMatrixElementInverseRef,
)
from .distance_matrix_element_price import DistanceMatrixElementPrice
from .distance_matrix_element_price_ref import DistanceMatrixElementPriceRef
from .distance_matrix_element_ref import DistanceMatrixElementRef
from .distribution_channel_ref import DistributionChannelRef
from .eligibility_change_policy_ref import EligibilityChangePolicyRef
from .entitlement_given_ref import EntitlementGivenRef
from .entitlement_product_ref import EntitlementProductRef
from .entitlement_required_ref import EntitlementRequiredRef
from .exchanging_ref import ExchangingRef
from .facility_set_ref import FacilitySetRef
from .fare_class_enumeration import FareClassEnumeration
from .fare_demand_factor_ref import FareDemandFactorRef
from .fare_price_ref import FarePriceRef
from .fare_price_versioned_child_structure import (
    FarePriceVersionedChildStructure,
)
from .fare_product_price import FareProductPrice
from .fare_product_price_ref import FareProductPriceRef
from .fare_product_ref import FareProductRef
from .fare_quota_factor_ref import FareQuotaFactorRef
from .fare_section_ref import FareSectionRef
from .fare_structure_element_price import FareStructureElementPrice
from .fare_structure_element_price_ref import FareStructureElementPriceRef
from .fare_structure_element_ref import FareStructureElementRef
from .fare_table_column_ref_structure import FareTableColumnRefStructure
from .fare_table_column_versioned_child_structure import (
    FareTableColumnsRelStructure,
)
from .fare_table_ref import FareTableRef
from .fare_table_row_ref_structure import FareTableRowRefStructure
from .fare_table_row_versioned_child_structure import FareTableRowsRelStructure
from .fare_table_specifics_structure import FareTableSpecificsStructure
from .flexible_line_ref import FlexibleLineRef
from .frequency_of_use_ref import FrequencyOfUseRef
from .fulfilment_method_price import FulfilmentMethodPrice
from .fulfilment_method_price_ref import FulfilmentMethodPriceRef
from .fulfilment_method_ref import FulfilmentMethodRef
from .general_organisation_ref import GeneralOrganisationRef
from .geographical_interval_price import GeographicalIntervalPrice
from .geographical_interval_price_ref import GeographicalIntervalPriceRef
from .geographical_interval_ref import GeographicalIntervalRef
from .geographical_structure_factor_ref import GeographicalStructureFactorRef
from .geographical_unit_price import GeographicalUnitPrice
from .geographical_unit_price_ref import GeographicalUnitPriceRef
from .group_of_distance_matrix_elements_ref import (
    GroupOfDistanceMatrixElementsRef,
)
from .group_of_distribution_channels_ref import GroupOfDistributionChannelsRef
from .group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)
from .group_of_lines_ref import GroupOfLinesRef
from .group_of_services_ref import GroupOfServicesRef
from .group_ticket_ref import GroupTicketRef
from .info_links_rel_structure import InfoLinksRelStructure
from .interchanging_ref import InterchangingRef
from .limiting_rule_ref import LimitingRuleRef
from .line_ref import LineRef
from .luggage_allowance_ref import LuggageAllowanceRef
from .management_agent_ref import ManagementAgentRef
from .minimum_stay_ref import MinimumStayRef
from .multilingual_string import MultilingualString
from .network_ref import NetworkRef
from .notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from .operator_ref import OperatorRef
from .organisation_ref import OrganisationRef
from .other_organisation_ref import OtherOrganisationRef
from .parking_charge_band_ref import ParkingChargeBandRef
from .parking_price_ref import ParkingPriceRef
from .parking_properties_ref import ParkingPropertiesRef
from .parking_ref import ParkingRef
from .parking_tariff_ref import ParkingTariffRef
from .parking_vehicle_enumeration import ParkingVehicleEnumeration
from .payment_method_enumeration import PaymentMethodEnumeration
from .penalty_policy_ref import PenaltyPolicyRef
from .point_of_interest_ref import PointOfInterestRef
from .preassigned_fare_product_ref import PreassignedFareProductRef
from .price_group_ref import PriceGroupRef
from .priceable_object_ref import PriceableObjectRef
from .priceable_object_refs_rel_structure import (
    PriceableObjectRefsRelStructure,
)
from .pricing_rule_ref import PricingRuleRef
from .pricing_service_ref import PricingServiceRef
from .private_code import PrivateCode
from .profile_parameter_ref import ProfileParameterRef
from .purchase_window_ref import PurchaseWindowRef
from .quality_structure_factor_price import QualityStructureFactorPrice
from .quality_structure_factor_price_ref import QualityStructureFactorPriceRef
from .quality_structure_factor_ref import QualityStructureFactorRef
from .refunding_ref import RefundingRef
from .relative_direction_enumeration import RelativeDirectionEnumeration
from .replacing_ref import ReplacingRef
from .reselling_ref import ResellingRef
from .reserving_ref import ReservingRef
from .retail_consortium_ref import RetailConsortiumRef
from .round_trip_ref import RoundTripRef
from .rounding_ref import RoundingRef
from .routing_ref import RoutingRef
from .routing_type_enumeration import RoutingTypeEnumeration
from .sale_discount_right_ref import SaleDiscountRightRef
from .sales_offer_package_element_ref import SalesOfferPackageElementRef
from .sales_offer_package_entitlement_given_ref import (
    SalesOfferPackageEntitlementGivenRef,
)
from .sales_offer_package_entitlement_required_ref import (
    SalesOfferPackageEntitlementRequiredRef,
)
from .sales_offer_package_price import SalesOfferPackagePrice
from .sales_offer_package_price_ref import SalesOfferPackagePriceRef
from .sales_offer_package_ref import SalesOfferPackageRef
from .series_constraint_price import SeriesConstraintPrice
from .series_constraint_price_ref import SeriesConstraintPriceRef
from .series_constraint_ref import SeriesConstraintRef
from .service_access_right_ref import ServiceAccessRightRef
from .service_facility_set_ref import ServiceFacilitySetRef
from .service_journey_ref import ServiceJourneyRef
from .service_site_ref import ServiceSiteRef
from .serviced_organisation_ref import ServicedOrganisationRef
from .site_facility_set_ref import SiteFacilitySetRef
from .site_ref import SiteRef
from .standard_fare_table import StandardFareTable
from .standard_fare_table_ref import StandardFareTableRef
from .step_limit_ref import StepLimitRef
from .stop_place_ref import StopPlaceRef
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)
from .subscribing_ref import SubscribingRef
from .supplement_product_ref import SupplementProductRef
from .suspending_ref import SuspendingRef
from .tariff_ref import TariffRef
from .tariff_zone_ref import TariffZoneRef
from .template_service_journey_ref import TemplateServiceJourneyRef
from .third_party_product_ref import ThirdPartyProductRef
from .time_interval_price import TimeIntervalPrice
from .time_interval_price_ref import TimeIntervalPriceRef
from .time_interval_ref import TimeIntervalRef
from .time_structure_factor_ref import TimeStructureFactorRef
from .time_unit_price import TimeUnitPrice
from .time_unit_price_ref import TimeUnitPriceRef
from .time_unit_ref import TimeUnitRef
from .train_number_ref import TrainNumberRef
from .train_ref import TrainRef
from .transferability_ref import TransferabilityRef
from .travel_agent_ref import TravelAgentRef
from .type_of_fare_product_ref import TypeOfFareProductRef
from .type_of_fare_structure_factor_ref import TypeOfFareStructureFactorRef
from .type_of_fare_table_ref import TypeOfFareTableRef
from .type_of_payment_method_ref import TypeOfPaymentMethodRef
from .type_of_product_category_ref import TypeOfProductCategoryRef
from .type_of_service_ref import TypeOfServiceRef
from .type_of_travel_document_ref import TypeOfTravelDocumentRef
from .usage_discount_right_ref import UsageDiscountRightRef
from .usage_parameter_price import UsageParameterPrice
from .usage_parameter_price_ref import UsageParameterPriceRef
from .usage_parameter_refs_rel_structure import UsageParameterRefsRelStructure
from .usage_validity_period_ref import UsageValidityPeriodRef
from .used_in_refs_rel_structure import UsedInRefsRelStructure
from .user_profile_ref import UserProfileRef
from .validable_element_price import ValidableElementPrice
from .validable_element_price_ref import ValidableElementPriceRef
from .validable_element_ref import ValidableElementRef
from .vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CellVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "Cell_VersionedChildStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice: Optional[
        Union[
            FarePriceVersionedChildStructure,
            CustomerPurchasePackagePriceRef,
            ParkingPriceRef,
            TimeIntervalPriceRef,
            TimeUnitPriceRef,
            QualityStructureFactorPriceRef,
            ControllableElementPriceRef,
            ValidableElementPriceRef,
            GeographicalIntervalPriceRef,
            GeographicalUnitPriceRef,
            UsageParameterPriceRef,
            SalesOfferPackagePriceRef,
            DistanceMatrixElementPriceRef,
            FareStructureElementPriceRef,
            FulfilmentMethodPriceRef,
            SeriesConstraintPriceRef,
            CappingRulePriceRef,
            FareProductPriceRef,
            FarePriceRef,
            CustomerPurchasePackagePrice,
            "ParkingPrice",
            SalesOfferPackagePrice,
            FulfilmentMethodPrice,
            CappingRulePrice,
            FareProductPrice,
            FareStructureElementPrice,
            TimeIntervalPrice,
            TimeUnitPrice,
            QualityStructureFactorPrice,
            ControllableElementPrice,
            ValidableElementPrice,
            UsageParameterPrice,
            DistanceMatrixElementPrice,
            GeographicalIntervalPrice,
            GeographicalUnitPrice,
            SeriesConstraintPrice,
            PriceGroupRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CellPrice",
                    "type": FarePriceVersionedChildStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerPurchasePackagePriceRef",
                    "type": CustomerPurchasePackagePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPriceRef",
                    "type": ParkingPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeIntervalPriceRef",
                    "type": TimeIntervalPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeUnitPriceRef",
                    "type": TimeUnitPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactorPriceRef",
                    "type": QualityStructureFactorPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElementPriceRef",
                    "type": ControllableElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidableElementPriceRef",
                    "type": ValidableElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalIntervalPriceRef",
                    "type": GeographicalIntervalPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalUnitPriceRef",
                    "type": GeographicalUnitPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageParameterPriceRef",
                    "type": UsageParameterPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackagePriceRef",
                    "type": SalesOfferPackagePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElementPriceRef",
                    "type": DistanceMatrixElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElementPriceRef",
                    "type": FareStructureElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FulfilmentMethodPriceRef",
                    "type": FulfilmentMethodPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeriesConstraintPriceRef",
                    "type": SeriesConstraintPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappingRulePriceRef",
                    "type": CappingRulePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareProductPriceRef",
                    "type": FareProductPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FarePriceRef",
                    "type": FarePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerPurchasePackagePrice",
                    "type": CustomerPurchasePackagePrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPrice",
                    "type": Type["ParkingPrice"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackagePrice",
                    "type": SalesOfferPackagePrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FulfilmentMethodPrice",
                    "type": FulfilmentMethodPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappingRulePrice",
                    "type": CappingRulePrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareProductPrice",
                    "type": FareProductPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElementPrice",
                    "type": FareStructureElementPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeIntervalPrice",
                    "type": TimeIntervalPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeUnitPrice",
                    "type": TimeUnitPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactorPrice",
                    "type": QualityStructureFactorPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElementPrice",
                    "type": ControllableElementPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidableElementPrice",
                    "type": ValidableElementPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageParameterPrice",
                    "type": UsageParameterPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElementPrice",
                    "type": DistanceMatrixElementPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalIntervalPrice",
                    "type": GeographicalIntervalPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalUnitPrice",
                    "type": GeographicalUnitPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeriesConstraintPrice",
                    "type": SeriesConstraintPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PriceGroupRef",
                    "type": PriceGroupRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    choice_1: List[
        Union[
            CustomerPurchasePackageElementRef,
            CustomerPurchasePackageRef,
            ControllableElementRef,
            ValidableElementRef,
            SalesOfferPackageEntitlementGivenRef,
            SalesOfferPackageEntitlementRequiredRef,
            MinimumStayRef,
            InterchangingRef,
            FrequencyOfUseRef,
            SuspendingRef,
            UsageValidityPeriodRef,
            StepLimitRef,
            RoutingRef,
            RoundTripRef,
            LuggageAllowanceRef,
            EntitlementGivenRef,
            EntitlementRequiredRef,
            EligibilityChangePolicyRef,
            GroupTicketRef,
            CommercialProfileRef,
            CompanionProfileRef,
            UserProfileRef,
            ProfileParameterRef,
            SubscribingRef,
            PenaltyPolicyRef,
            ChargingPolicyRef,
            TransferabilityRef,
            ReplacingRef,
            RefundingRef,
            ExchangingRef,
            ResellingRef,
            CancellingRef,
            ReservingRef,
            PurchaseWindowRef,
            SalesOfferPackageElementRef,
            SalesOfferPackageRef,
            DistanceMatrixElementInverseRef,
            DistanceMatrixElementRef,
            FareStructureElementRef,
            FulfilmentMethodRef,
            SeriesConstraintRef,
            CappingRuleRef,
            EntitlementProductRef,
            SupplementProductRef,
            PreassignedFareProductRef,
            AmountOfPriceUnitProductRef,
            UsageDiscountRightRef,
            ThirdPartyProductRef,
            CappedDiscountRightRef,
            SaleDiscountRightRef,
            FareProductRef,
            ServiceAccessRightRef,
            TimeIntervalRef,
            GeographicalIntervalRef,
            ParkingChargeBandRef,
            TimeStructureFactorRef,
            FareQuotaFactorRef,
            FareDemandFactorRef,
            QualityStructureFactorRef,
            GeographicalStructureFactorRef,
            PriceableObjectRef,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CustomerPurchasePackageElementRef",
                    "type": CustomerPurchasePackageElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerPurchasePackageRef",
                    "type": CustomerPurchasePackageRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElementRef",
                    "type": ControllableElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidableElementRef",
                    "type": ValidableElementRef,
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
                    "name": "PurchaseWindowRef",
                    "type": PurchaseWindowRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageElementRef",
                    "type": SalesOfferPackageElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageRef",
                    "type": SalesOfferPackageRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElementInverseRef",
                    "type": DistanceMatrixElementInverseRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElementRef",
                    "type": DistanceMatrixElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElementRef",
                    "type": FareStructureElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FulfilmentMethodRef",
                    "type": FulfilmentMethodRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeriesConstraintRef",
                    "type": SeriesConstraintRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappingRuleRef",
                    "type": CappingRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntitlementProductRef",
                    "type": EntitlementProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SupplementProductRef",
                    "type": SupplementProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PreassignedFareProductRef",
                    "type": PreassignedFareProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AmountOfPriceUnitProductRef",
                    "type": AmountOfPriceUnitProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageDiscountRightRef",
                    "type": UsageDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ThirdPartyProductRef",
                    "type": ThirdPartyProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappedDiscountRightRef",
                    "type": CappedDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SaleDiscountRightRef",
                    "type": SaleDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareProductRef",
                    "type": FareProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceAccessRightRef",
                    "type": ServiceAccessRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeIntervalRef",
                    "type": TimeIntervalRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalIntervalRef",
                    "type": GeographicalIntervalRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingChargeBandRef",
                    "type": ParkingChargeBandRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeStructureFactorRef",
                    "type": TimeStructureFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareQuotaFactorRef",
                    "type": FareQuotaFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareDemandFactorRef",
                    "type": FareDemandFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactorRef",
                    "type": QualityStructureFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalStructureFactorRef",
                    "type": GeographicalStructureFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PriceableObjectRef",
                    "type": PriceableObjectRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    group_of_distance_matrix_elements_ref: Optional[
        GroupOfDistanceMatrixElementsRef
    ] = field(
        default=None,
        metadata={
            "name": "GroupOfDistanceMatrixElementsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    direction_type: Optional[RelativeDirectionEnumeration] = field(
        default=None,
        metadata={
            "name": "DirectionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    routing_type: Optional[RoutingTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "RoutingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    operator_ref: Optional[OperatorRef] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    network_ref_or_group_of_lines_ref: Optional[
        Union[NetworkRef, GroupOfLinesRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "NetworkRef",
                    "type": NetworkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfLinesRef",
                    "type": GroupOfLinesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    flexible_line_ref_or_line_ref: Optional[
        Union[FlexibleLineRef, LineRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleLineRef",
                    "type": FlexibleLineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineRef",
                    "type": LineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    choice_2: Optional[
        Union[
            StopPlaceRef,
            ParkingRef,
            PointOfInterestRef,
            ServiceSiteRef,
            SiteRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StopPlaceRef",
                    "type": StopPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingRef",
                    "type": ParkingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestRef",
                    "type": PointOfInterestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceSiteRef",
                    "type": ServiceSiteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteRef",
                    "type": SiteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    tariff_zone_ref: Optional[TariffZoneRef] = field(
        default=None,
        metadata={
            "name": "TariffZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_section_ref: Optional[FareSectionRef] = field(
        default=None,
        metadata={
            "name": "FareSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_class: Optional[FareClassEnumeration] = field(
        default=None,
        metadata={
            "name": "FareClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    class_of_use_ref: Optional[ClassOfUseRef] = field(
        default=None,
        metadata={
            "name": "ClassOfUseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    service_facility_set_ref_or_site_facility_set_ref_or_facility_set_ref: Optional[
        Union[ServiceFacilitySetRef, SiteFacilitySetRef, FacilitySetRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceFacilitySetRef",
                    "type": ServiceFacilitySetRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteFacilitySetRef",
                    "type": SiteFacilitySetRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FacilitySetRef",
                    "type": FacilitySetRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    type_of_product_category_ref: Optional[TypeOfProductCategoryRef] = field(
        default=None,
        metadata={
            "name": "TypeOfProductCategoryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_service_ref: Optional[TypeOfServiceRef] = field(
        default=None,
        metadata={
            "name": "TypeOfServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice_3: Optional[
        Union[
            TemplateServiceJourneyRef,
            ServiceJourneyRef,
            TrainNumberRef,
            GroupOfServicesRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TemplateServiceJourneyRef",
                    "type": TemplateServiceJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyRef",
                    "type": ServiceJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainNumberRef",
                    "type": TrainNumberRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfServicesRef",
                    "type": GroupOfServicesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    type_of_fare_product_ref: Optional[TypeOfFareProductRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    distribution_channel_ref_or_group_of_distribution_channels_ref: Optional[
        Union[DistributionChannelRef, GroupOfDistributionChannelsRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DistributionChannelRef",
                    "type": DistributionChannelRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfDistributionChannelsRef",
                    "type": GroupOfDistributionChannelsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    payment_method: Optional[PaymentMethodEnumeration] = field(
        default=None,
        metadata={
            "name": "PaymentMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_payment_method_ref: Optional[TypeOfPaymentMethodRef] = field(
        default=None,
        metadata={
            "name": "TypeOfPaymentMethodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_travel_document_ref: Optional[TypeOfTravelDocumentRef] = field(
        default=None,
        metadata={
            "name": "TypeOfTravelDocumentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    standard_fare_table_ref_or_fare_table_ref: Optional[
        Union[StandardFareTableRef, FareTableRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StandardFareTableRef",
                    "type": StandardFareTableRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareTableRef",
                    "type": FareTableRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    column_ref: Optional[FareTableColumnRefStructure] = field(
        default=None,
        metadata={
            "name": "ColumnRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    row_ref: Optional[FareTableRowRefStructure] = field(
        default=None,
        metadata={
            "name": "RowRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    notice_assignments: Optional[NoticeAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ParkingPriceVersionedChildStructure(FarePriceVersionedChildStructure):
    class Meta:
        name = "ParkingPrice_VersionedChildStructure"

    parking_tariff_ref_or_parking_charge_band: Optional[
        Union[ParkingTariffRef, "ParkingChargeBand"]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ParkingTariffRef",
                    "type": ParkingTariffRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingChargeBand",
                    "type": Type["ParkingChargeBand"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )


@dataclass
class Cell(CellVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class ParkingPrice(ParkingPriceVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class CellsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "cells_RelStructure"

    choice: List[
        Union[
            Cell,
            CellVersionedChildStructure,
            CustomerPurchasePackagePrice,
            "ParkingPrice",
            SalesOfferPackagePrice,
            FulfilmentMethodPrice,
            CappingRulePrice,
            FareProductPrice,
            FareStructureElementPrice,
            TimeIntervalPrice,
            TimeUnitPrice,
            QualityStructureFactorPrice,
            ControllableElementPrice,
            ValidableElementPrice,
            UsageParameterPrice,
            DistanceMatrixElementPrice,
            GeographicalIntervalPrice,
            GeographicalUnitPrice,
            SeriesConstraintPrice,
            CustomerPurchasePackagePriceRef,
            ParkingPriceRef,
            TimeIntervalPriceRef,
            TimeUnitPriceRef,
            QualityStructureFactorPriceRef,
            ControllableElementPriceRef,
            ValidableElementPriceRef,
            GeographicalIntervalPriceRef,
            GeographicalUnitPriceRef,
            UsageParameterPriceRef,
            SalesOfferPackagePriceRef,
            DistanceMatrixElementPriceRef,
            FareStructureElementPriceRef,
            FulfilmentMethodPriceRef,
            SeriesConstraintPriceRef,
            CappingRulePriceRef,
            FareProductPriceRef,
            FarePriceRef,
            CellRef,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Cell",
                    "type": Cell,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CellInContext",
                    "type": CellVersionedChildStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerPurchasePackagePrice",
                    "type": CustomerPurchasePackagePrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPrice",
                    "type": Type["ParkingPrice"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackagePrice",
                    "type": SalesOfferPackagePrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FulfilmentMethodPrice",
                    "type": FulfilmentMethodPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappingRulePrice",
                    "type": CappingRulePrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareProductPrice",
                    "type": FareProductPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElementPrice",
                    "type": FareStructureElementPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeIntervalPrice",
                    "type": TimeIntervalPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeUnitPrice",
                    "type": TimeUnitPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactorPrice",
                    "type": QualityStructureFactorPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElementPrice",
                    "type": ControllableElementPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidableElementPrice",
                    "type": ValidableElementPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageParameterPrice",
                    "type": UsageParameterPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElementPrice",
                    "type": DistanceMatrixElementPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalIntervalPrice",
                    "type": GeographicalIntervalPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalUnitPrice",
                    "type": GeographicalUnitPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeriesConstraintPrice",
                    "type": SeriesConstraintPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerPurchasePackagePriceRef",
                    "type": CustomerPurchasePackagePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPriceRef",
                    "type": ParkingPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeIntervalPriceRef",
                    "type": TimeIntervalPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeUnitPriceRef",
                    "type": TimeUnitPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactorPriceRef",
                    "type": QualityStructureFactorPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElementPriceRef",
                    "type": ControllableElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidableElementPriceRef",
                    "type": ValidableElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalIntervalPriceRef",
                    "type": GeographicalIntervalPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalUnitPriceRef",
                    "type": GeographicalUnitPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageParameterPriceRef",
                    "type": UsageParameterPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackagePriceRef",
                    "type": SalesOfferPackagePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElementPriceRef",
                    "type": DistanceMatrixElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElementPriceRef",
                    "type": FareStructureElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FulfilmentMethodPriceRef",
                    "type": FulfilmentMethodPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeriesConstraintPriceRef",
                    "type": SeriesConstraintPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappingRulePriceRef",
                    "type": CappingRulePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareProductPriceRef",
                    "type": FareProductPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FarePriceRef",
                    "type": FarePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CellRef",
                    "type": CellRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )


@dataclass
class FarePricesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "farePrices_RelStructure"

    choice: List[
        Union[
            CustomerPurchasePackagePriceRef,
            ParkingPriceRef,
            TimeIntervalPriceRef,
            TimeUnitPriceRef,
            QualityStructureFactorPriceRef,
            ControllableElementPriceRef,
            ValidableElementPriceRef,
            GeographicalIntervalPriceRef,
            GeographicalUnitPriceRef,
            UsageParameterPriceRef,
            SalesOfferPackagePriceRef,
            DistanceMatrixElementPriceRef,
            FareStructureElementPriceRef,
            FulfilmentMethodPriceRef,
            SeriesConstraintPriceRef,
            CappingRulePriceRef,
            FareProductPriceRef,
            FarePriceRef,
            CellRef,
            CustomerPurchasePackagePrice,
            ParkingPrice,
            SalesOfferPackagePrice,
            FulfilmentMethodPrice,
            CappingRulePrice,
            FareProductPrice,
            FareStructureElementPrice,
            TimeIntervalPrice,
            TimeUnitPrice,
            QualityStructureFactorPrice,
            ControllableElementPrice,
            ValidableElementPrice,
            UsageParameterPrice,
            DistanceMatrixElementPrice,
            GeographicalIntervalPrice,
            GeographicalUnitPrice,
            SeriesConstraintPrice,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CustomerPurchasePackagePriceRef",
                    "type": CustomerPurchasePackagePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPriceRef",
                    "type": ParkingPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeIntervalPriceRef",
                    "type": TimeIntervalPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeUnitPriceRef",
                    "type": TimeUnitPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactorPriceRef",
                    "type": QualityStructureFactorPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElementPriceRef",
                    "type": ControllableElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidableElementPriceRef",
                    "type": ValidableElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalIntervalPriceRef",
                    "type": GeographicalIntervalPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalUnitPriceRef",
                    "type": GeographicalUnitPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageParameterPriceRef",
                    "type": UsageParameterPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackagePriceRef",
                    "type": SalesOfferPackagePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElementPriceRef",
                    "type": DistanceMatrixElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElementPriceRef",
                    "type": FareStructureElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FulfilmentMethodPriceRef",
                    "type": FulfilmentMethodPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeriesConstraintPriceRef",
                    "type": SeriesConstraintPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappingRulePriceRef",
                    "type": CappingRulePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareProductPriceRef",
                    "type": FareProductPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FarePriceRef",
                    "type": FarePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CellRef",
                    "type": CellRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerPurchasePackagePrice",
                    "type": CustomerPurchasePackagePrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPrice",
                    "type": ParkingPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackagePrice",
                    "type": SalesOfferPackagePrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FulfilmentMethodPrice",
                    "type": FulfilmentMethodPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappingRulePrice",
                    "type": CappingRulePrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareProductPrice",
                    "type": FareProductPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElementPrice",
                    "type": FareStructureElementPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeIntervalPrice",
                    "type": TimeIntervalPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeUnitPrice",
                    "type": TimeUnitPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactorPrice",
                    "type": QualityStructureFactorPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElementPrice",
                    "type": ControllableElementPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidableElementPrice",
                    "type": ValidableElementPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageParameterPrice",
                    "type": UsageParameterPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElementPrice",
                    "type": DistanceMatrixElementPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalIntervalPrice",
                    "type": GeographicalIntervalPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalUnitPrice",
                    "type": GeographicalUnitPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeriesConstraintPrice",
                    "type": SeriesConstraintPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )


@dataclass
class FareTableVersionStructure(GroupOfEntitiesVersionStructure):
    class Meta:
        name = "FareTable_VersionStructure"

    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    rounding_ref: Optional[RoundingRef] = field(
        default=None,
        metadata={
            "name": "RoundingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_fare_table_ref: Optional[TypeOfFareTableRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFareTableRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    prices_for: Optional[PriceableObjectRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "pricesFor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    used_in: Optional[UsedInRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "usedIn",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice: Optional[
        Union[
            RetailConsortiumRef,
            AuthorityRef,
            OperatorRef,
            GeneralOrganisationRef,
            ManagementAgentRef,
            ServicedOrganisationRef,
            TravelAgentRef,
            OtherOrganisationRef,
            OrganisationRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RetailConsortiumRef",
                    "type": RetailConsortiumRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AuthorityRef",
                    "type": AuthorityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatorRef",
                    "type": OperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralOrganisationRef",
                    "type": GeneralOrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ManagementAgentRef",
                    "type": ManagementAgentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicedOrganisationRef",
                    "type": ServicedOrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelAgentRef",
                    "type": TravelAgentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OtherOrganisationRef",
                    "type": OtherOrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationRef",
                    "type": OrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    limitations: Optional[UsageParameterRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    specifics: Optional[FareTableSpecificsStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    columns: Optional[FareTableColumnsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    rows: Optional[FareTableRowsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    includes: Optional["FareTablesRelStructure"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    embargo_until: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EmbargoUntil",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    prices: Optional["FarePricesRelStructure"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    cells: Optional[CellsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    notice_assignments: Optional[NoticeAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass
class PriceGroupVersionStructure(GroupOfEntitiesVersionStructure):
    class Meta:
        name = "PriceGroup_VersionStructure"

    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    rounding_ref: Optional[RoundingRef] = field(
        default=None,
        metadata={
            "name": "RoundingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    members: Optional[FarePricesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice: Optional[
        Union[
            CustomerPurchasePackagePriceRef,
            ParkingPriceRef,
            TimeIntervalPriceRef,
            TimeUnitPriceRef,
            QualityStructureFactorPriceRef,
            ControllableElementPriceRef,
            ValidableElementPriceRef,
            GeographicalIntervalPriceRef,
            GeographicalUnitPriceRef,
            UsageParameterPriceRef,
            SalesOfferPackagePriceRef,
            DistanceMatrixElementPriceRef,
            FareStructureElementPriceRef,
            FulfilmentMethodPriceRef,
            SeriesConstraintPriceRef,
            CappingRulePriceRef,
            FareProductPriceRef,
            FarePriceRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CustomerPurchasePackagePriceRef",
                    "type": CustomerPurchasePackagePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPriceRef",
                    "type": ParkingPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeIntervalPriceRef",
                    "type": TimeIntervalPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeUnitPriceRef",
                    "type": TimeUnitPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactorPriceRef",
                    "type": QualityStructureFactorPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElementPriceRef",
                    "type": ControllableElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidableElementPriceRef",
                    "type": ValidableElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalIntervalPriceRef",
                    "type": GeographicalIntervalPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalUnitPriceRef",
                    "type": GeographicalUnitPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageParameterPriceRef",
                    "type": UsageParameterPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackagePriceRef",
                    "type": SalesOfferPackagePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElementPriceRef",
                    "type": DistanceMatrixElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElementPriceRef",
                    "type": FareStructureElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FulfilmentMethodPriceRef",
                    "type": FulfilmentMethodPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeriesConstraintPriceRef",
                    "type": SeriesConstraintPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappingRulePriceRef",
                    "type": CappingRulePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareProductPriceRef",
                    "type": FareProductPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FarePriceRef",
                    "type": FarePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )


@dataclass
class FareTable(FareTableVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class FareTableInContext(FareTableVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class PriceGroup(PriceGroupVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class FareTablesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "fareTables_RelStructure"

    choice: List[
        Union[
            StandardFareTableRef,
            FareTableRef,
            StandardFareTable,
            FareTableInContext,
            FareTable,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StandardFareTableRef",
                    "type": StandardFareTableRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareTableRef",
                    "type": FareTableRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StandardFareTable",
                    "type": StandardFareTable,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareTableInContext",
                    "type": FareTableInContext,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareTable",
                    "type": FareTable,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )


@dataclass
class PriceGroupsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "priceGroups_RelStructure"

    price_group_ref_or_price_group: List[
        Union[PriceGroupRef, PriceGroup]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PriceGroupRef",
                    "type": PriceGroupRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PriceGroup",
                    "type": PriceGroup,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )


@dataclass
class PriceableObjectVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "PriceableObject_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "Url",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    info_links: Optional[InfoLinksRelStructure] = field(
        default=None,
        metadata={
            "name": "infoLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    alternative_names: Optional[AlternativeNamesRelStructure] = field(
        default=None,
        metadata={
            "name": "alternativeNames",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    notice_assignments: Optional[NoticeAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    pricing_service_ref: Optional[PricingServiceRef] = field(
        default=None,
        metadata={
            "name": "PricingServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    limiting_rule_ref_or_discounting_rule_ref_or_pricing_rule_ref: Optional[
        Union[LimitingRuleRef, DiscountingRuleRef, PricingRuleRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "LimitingRuleRef",
                    "type": LimitingRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DiscountingRuleRef",
                    "type": DiscountingRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PricingRuleRef",
                    "type": PricingRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    price_groups: Optional[PriceGroupsRelStructure] = field(
        default=None,
        metadata={
            "name": "priceGroups",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_tables: Optional[FareTablesRelStructure] = field(
        default=None,
        metadata={
            "name": "fareTables",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass
class FareStructureFactorVersionStructure(PriceableObjectVersionStructure):
    class Meta:
        name = "FareStructureFactor_VersionStructure"

    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_fare_structure_factor_ref: Optional[
        TypeOfFareStructureFactorRef
    ] = field(
        default=None,
        metadata={
            "name": "TypeOfFareStructureFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    factor: Optional[object] = field(
        default=None,
        metadata={
            "name": "Factor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass
class TimeStructureFactorVersionStructure(FareStructureFactorVersionStructure):
    class Meta:
        name = "TimeStructureFactor_VersionStructure"

    parking_tariff_ref_or_tariff_ref: Optional[
        Union[ParkingTariffRef, TariffRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ParkingTariffRef",
                    "type": ParkingTariffRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TariffRef",
                    "type": TariffRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    time_interval_ref: Optional[TimeIntervalRef] = field(
        default=None,
        metadata={
            "name": "TimeIntervalRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    time_unit_ref: Optional[TimeUnitRef] = field(
        default=None,
        metadata={
            "name": "TimeUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_quota_factor_ref_or_fare_demand_factor_ref_or_quality_structure_factor_ref: Optional[
        Union[
            FareQuotaFactorRef, FareDemandFactorRef, QualityStructureFactorRef
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareQuotaFactorRef",
                    "type": FareQuotaFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareDemandFactorRef",
                    "type": FareDemandFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactorRef",
                    "type": QualityStructureFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )


@dataclass
class ParkingChargeBandVersionStructure(TimeStructureFactorVersionStructure):
    class Meta:
        name = "ParkingChargeBand_VersionStructure"

    parking_properties_ref: Optional[ParkingPropertiesRef] = field(
        default=None,
        metadata={
            "name": "ParkingPropertiesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_vehicle_type: Optional[ParkingVehicleEnumeration] = field(
        default=None,
        metadata={
            "name": "ParkingVehicleType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    compound_train_ref_or_train_ref_or_vehicle_type_ref: Optional[
        Union[CompoundTrainRef, TrainRef, VehicleTypeRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CompoundTrainRef",
                    "type": CompoundTrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainRef",
                    "type": TrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleTypeRef",
                    "type": VehicleTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    maximum_stay: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumStay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    prices: Optional["FarePricesRelStructure"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass
class ParkingChargeBand(ParkingChargeBandVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
