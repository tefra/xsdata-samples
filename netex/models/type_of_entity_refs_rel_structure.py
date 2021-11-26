from dataclasses import dataclass, field
from typing import List
from .all_distribution_channels_ref import AllDistributionChannelsRef
from .customer_account_status_ref import CustomerAccountStatusRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .type_of_access_right_assignment_ref import TypeOfAccessRightAssignmentRef
from .type_of_congestion_ref import TypeOfCongestionRef
from .type_of_customer_account_ref import TypeOfCustomerAccountRef
from .type_of_delivery_variant_ref import TypeOfDeliveryVariantRef
from .type_of_equipment_ref import TypeOfEquipmentRef
from .type_of_facility_ref import TypeOfFacilityRef
from .type_of_fare_contract_entry_ref import TypeOfFareContractEntryRef
from .type_of_fare_contract_ref import TypeOfFareContractRef
from .type_of_fare_product_ref import TypeOfFareProductRef
from .type_of_fare_structure_element_ref import TypeOfFareStructureElementRef
from .type_of_fare_structure_factor_ref import TypeOfFareStructureFactorRef
from .type_of_feature_ref import TypeOfFeatureRef
from .type_of_flexible_service_ref import TypeOfFlexibleServiceRef
from .type_of_frame_ref import TypeOfFrameRef
from .type_of_journey_pattern_ref import TypeOfJourneyPatternRef
from .type_of_line_ref import TypeOfLineRef
from .type_of_link_ref import TypeOfLinkRef
from .type_of_link_sequence_ref import TypeOfLinkSequenceRef
from .type_of_machine_readability_ref import TypeOfMachineReadabilityRef
from .type_of_notice_ref import TypeOfNoticeRef
from .type_of_organisation_part_ref import TypeOfOrganisationPartRef
from .type_of_organisation_ref import TypeOfOrganisationRef
from .type_of_passenger_information_equipment_ref import TypeOfPassengerInformationEquipmentRef
from .type_of_place_ref import TypeOfPlaceRef
from .type_of_point_ref import TypeOfPointRef
from .type_of_pricing_rule_ref import TypeOfPricingRuleRef
from .type_of_projection_ref import TypeOfProjectionRef
from .type_of_retail_device_ref import TypeOfRetailDeviceRef
from .type_of_sales_offer_package_ref import TypeOfSalesOfferPackageRef
from .type_of_security_list_ref import TypeOfSecurityListRef
from .type_of_service_feature_ref import TypeOfServiceFeatureRef
from .type_of_service_ref import TypeOfServiceRef
from .type_of_tariff_ref import TypeOfTariffRef
from .type_of_time_demand_type_ref import TypeOfTimeDemandTypeRef
from .type_of_transfer_ref import TypeOfTransferRef
from .type_of_travel_document_ref import TypeOfTravelDocumentRef
from .type_of_validity_ref import TypeOfValidityRef
from .type_of_zone_ref import TypeOfZoneRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfEntityRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "typeOfEntityRefs_RelStructure"

    type_of_retail_device_ref: List[TypeOfRetailDeviceRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfRetailDeviceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_account_status_ref: List[CustomerAccountStatusRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerAccountStatusRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_customer_account_ref: List[TypeOfCustomerAccountRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfCustomerAccountRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_fare_contract_entry_ref: List[TypeOfFareContractEntryRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareContractEntryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_fare_contract_ref: List[TypeOfFareContractRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareContractRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_access_right_assignment_ref: List[TypeOfAccessRightAssignmentRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfAccessRightAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_sales_offer_package_ref: List[TypeOfSalesOfferPackageRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfSalesOfferPackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_fare_structure_element_ref: List[TypeOfFareStructureElementRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareStructureElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_tariff_ref: List[TypeOfTariffRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfTariffRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    all_distribution_channels_ref: List[AllDistributionChannelsRef] = field(
        default_factory=list,
        metadata={
            "name": "AllDistributionChannelsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_machine_readability_ref: List[TypeOfMachineReadabilityRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfMachineReadabilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_travel_document_ref: List[TypeOfTravelDocumentRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfTravelDocumentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_fare_product_ref: List[TypeOfFareProductRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_fare_structure_factor_ref: List[TypeOfFareStructureFactorRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareStructureFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_pricing_rule_ref: List[TypeOfPricingRuleRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPricingRuleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_flexible_service_ref: List[TypeOfFlexibleServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFlexibleServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_passenger_information_equipment_ref: List[TypeOfPassengerInformationEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPassengerInformationEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_service_feature_ref: List[TypeOfServiceFeatureRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfServiceFeatureRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_congestion_ref: List[TypeOfCongestionRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfCongestionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_time_demand_type_ref: List[TypeOfTimeDemandTypeRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfTimeDemandTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_journey_pattern_ref: List[TypeOfJourneyPatternRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_security_list_ref: List[TypeOfSecurityListRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfSecurityListRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_delivery_variant_ref: List[TypeOfDeliveryVariantRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfDeliveryVariantRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_notice_ref: List[TypeOfNoticeRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfNoticeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_service_ref: List[TypeOfServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_facility_ref: List[TypeOfFacilityRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFacilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_equipment_ref: List[TypeOfEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_projection_ref: List[TypeOfProjectionRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfProjectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_feature_ref: List[TypeOfFeatureRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFeatureRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_link_sequence_ref: List[TypeOfLinkSequenceRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfLinkSequenceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_organisation_part_ref: List[TypeOfOrganisationPartRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfOrganisationPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_organisation_ref: List[TypeOfOrganisationRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_place_ref: List[TypeOfPlaceRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_transfer_ref: List[TypeOfTransferRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfTransferRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_zone_ref: List[TypeOfZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_link_ref: List[TypeOfLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_point_ref: List[TypeOfPointRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_line_ref: List[TypeOfLineRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfLineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_validity_ref: List[TypeOfValidityRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfValidityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_frame_ref: List[TypeOfFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
