from dataclasses import dataclass, field
from typing import List
from .branding import Branding
from .charging_moment import ChargingMoment
from .class_of_use import ClassOfUse
from .customer_account_status import CustomerAccountStatus
from .data_source import DataSource
from .direction import Direction
from .open_transport_mode import OpenTransportMode
from .point_of_interest_classification import PointOfInterestClassification
from .price_unit import PriceUnit
from .purpose_of_equipment_profile import PurposeOfEquipmentProfile
from .purpose_of_grouping import PurposeOfGrouping
from .purpose_of_journey_partition import PurposeOfJourneyPartition
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from .submode import Submode
from .timing_algorithm_type import TimingAlgorithmType
from .type_of_access_right_assignment import TypeOfAccessRightAssignment
from .type_of_activation import TypeOfActivation
from .type_of_codespace_assignment import TypeOfCodespaceAssignment
from .type_of_concession import TypeOfConcession
from .type_of_congestion import TypeOfCongestion
from .type_of_customer_account import TypeOfCustomerAccount
from .type_of_delivery_variant import TypeOfDeliveryVariant
from .type_of_entity import TypeOfEntity
from .type_of_equipment import TypeOfEquipment
from .type_of_facility import TypeOfFacility
from .type_of_fare_contract import TypeOfFareContract
from .type_of_fare_contract_entry import TypeOfFareContractEntry
from .type_of_fare_product import TypeOfFareProduct
from .type_of_fare_structure_element import TypeOfFareStructureElement
from .type_of_fare_structure_factor import TypeOfFareStructureFactor
from .type_of_fare_table import TypeOfFareTable
from .type_of_feature import TypeOfFeature
from .type_of_flexible_service import TypeOfFlexibleService
from .type_of_journey_pattern import TypeOfJourneyPattern
from .type_of_line import TypeOfLine
from .type_of_link import TypeOfLink
from .type_of_link_sequence import TypeOfLinkSequence
from .type_of_machine_readability import TypeOfMachineReadability
from .type_of_notice import TypeOfNotice
from .type_of_operation import TypeOfOperation
from .type_of_organisation import TypeOfOrganisation
from .type_of_organisation_part import TypeOfOrganisationPart
from .type_of_passenger_information_equipment import TypeOfPassengerInformationEquipment
from .type_of_payment_method import TypeOfPaymentMethod
from .type_of_place import TypeOfPlace
from .type_of_point import TypeOfPoint
from .type_of_pricing_rule import TypeOfPricingRule
from .type_of_product_category import TypeOfProductCategory
from .type_of_projection import TypeOfProjection
from .type_of_responsibility_role import TypeOfResponsibilityRole
from .type_of_retail_device import TypeOfRetailDevice
from .type_of_sales_offer_package import TypeOfSalesOfferPackage
from .type_of_security_list import TypeOfSecurityList
from .type_of_service import TypeOfService
from .type_of_service_feature import TypeOfServiceFeature
from .type_of_tariff import TypeOfTariff
from .type_of_time_demand_type import TypeOfTimeDemandType
from .type_of_transfer import TypeOfTransfer
from .type_of_travel_document import TypeOfTravelDocument
from .type_of_usage_parameter import TypeOfUsageParameter
from .type_of_validity import TypeOfValidity
from .type_of_value import TypeOfValue
from .type_of_version import TypeOfVersion
from .type_of_zone import TypeOfZone
from .types_of_frame_rel_structure import TypeOfFrame

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypesOfValueStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "typesOfValueStructure"

    type_of_machine_readability: List[TypeOfMachineReadability] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfMachineReadability",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_concession: List[TypeOfConcession] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfConcession",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    charging_moment: List[ChargingMoment] = field(
        default_factory=list,
        metadata={
            "name": "ChargingMoment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_usage_parameter: List[TypeOfUsageParameter] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfUsageParameter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_fare_table: List[TypeOfFareTable] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareTable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_pricing_rule: List[TypeOfPricingRule] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPricingRule",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    price_unit: List[PriceUnit] = field(
        default_factory=list,
        metadata={
            "name": "PriceUnit",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    timing_algorithm_type: List[TimingAlgorithmType] = field(
        default_factory=list,
        metadata={
            "name": "TimingAlgorithmType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    purpose_of_journey_partition: List[PurposeOfJourneyPartition] = field(
        default_factory=list,
        metadata={
            "name": "PurposeOfJourneyPartition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_service_feature: List[TypeOfServiceFeature] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfServiceFeature",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    point_of_interest_classification: List[PointOfInterestClassification] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestClassification",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    direction: List[Direction] = field(
        default_factory=list,
        metadata={
            "name": "Direction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    purpose_of_equipment_profile: List[PurposeOfEquipmentProfile] = field(
        default_factory=list,
        metadata={
            "name": "PurposeOfEquipmentProfile",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_security_list: List[TypeOfSecurityList] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfSecurityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_product_category: List[TypeOfProductCategory] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfProductCategory",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_payment_method: List[TypeOfPaymentMethod] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPaymentMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    class_of_use: List[ClassOfUse] = field(
        default_factory=list,
        metadata={
            "name": "ClassOfUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    submode: List[Submode] = field(
        default_factory=list,
        metadata={
            "name": "Submode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    open_transport_mode: List[OpenTransportMode] = field(
        default_factory=list,
        metadata={
            "name": "OpenTransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_codespace_assignment: List[TypeOfCodespaceAssignment] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfCodespaceAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_validity: List[TypeOfValidity] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfValidity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    purpose_of_grouping: List[PurposeOfGrouping] = field(
        default_factory=list,
        metadata={
            "name": "PurposeOfGrouping",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    branding: List[Branding] = field(
        default_factory=list,
        metadata={
            "name": "Branding",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    data_source: List[DataSource] = field(
        default_factory=list,
        metadata={
            "name": "DataSource",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_retail_device: List[TypeOfRetailDevice] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfRetailDevice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    customer_account_status: List[CustomerAccountStatus] = field(
        default_factory=list,
        metadata={
            "name": "CustomerAccountStatus",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_customer_account: List[TypeOfCustomerAccount] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfCustomerAccount",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_fare_contract_entry: List[TypeOfFareContractEntry] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareContractEntry",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_fare_contract: List[TypeOfFareContract] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareContract",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_travel_document: List[TypeOfTravelDocument] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfTravelDocument",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_sales_offer_package: List[TypeOfSalesOfferPackage] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfSalesOfferPackage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_fare_product: List[TypeOfFareProduct] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_fare_structure_element: List[TypeOfFareStructureElement] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareStructureElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_tariff: List[TypeOfTariff] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfTariff",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_access_right_assignment: List[TypeOfAccessRightAssignment] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfAccessRightAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_fare_structure_factor: List[TypeOfFareStructureFactor] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareStructureFactor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_flexible_service: List[TypeOfFlexibleService] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFlexibleService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_time_demand_type: List[TypeOfTimeDemandType] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfTimeDemandType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_passenger_information_equipment: List[TypeOfPassengerInformationEquipment] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPassengerInformationEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_congestion: List[TypeOfCongestion] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfCongestion",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_journey_pattern: List[TypeOfJourneyPattern] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfJourneyPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_line: List[TypeOfLine] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfLine",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_activation: List[TypeOfActivation] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfActivation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_delivery_variant: List[TypeOfDeliveryVariant] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfDeliveryVariant",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_notice: List[TypeOfNotice] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfNotice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_facility: List[TypeOfFacility] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFacility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_service: List[TypeOfService] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_equipment: List[TypeOfEquipment] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_feature: List[TypeOfFeature] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFeature",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_link_sequence: List[TypeOfLinkSequence] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfLinkSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_place: List[TypeOfPlace] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_transfer: List[TypeOfTransfer] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfTransfer",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_operation: List[TypeOfOperation] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfOperation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_organisation_part: List[TypeOfOrganisationPart] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfOrganisationPart",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_organisation: List[TypeOfOrganisation] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfOrganisation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_zone: List[TypeOfZone] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_link: List[TypeOfLink] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_point: List[TypeOfPoint] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_projection: List[TypeOfProjection] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfProjection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_frame: List[TypeOfFrame] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_responsibility_role: List[TypeOfResponsibilityRole] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfResponsibilityRole",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_entity: List[TypeOfEntity] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfEntity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_version: List[TypeOfVersion] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfVersion",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    type_of_value: List[TypeOfValue] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
