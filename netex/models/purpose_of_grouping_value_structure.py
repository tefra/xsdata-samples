from __future__ import annotations

from dataclasses import dataclass, field

from .class_refs_rel_structure import ClassRefsRelStructure
from .customer_account_status import CustomerAccountStatus
from .type_of_access_right_assignment import TypeOfAccessRightAssignment
from .type_of_activation import TypeOfActivation
from .type_of_battery_chemistry import TypeOfBatteryChemistry
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
from .type_of_feature import TypeOfFeature
from .type_of_flexible_service import TypeOfFlexibleService
from .type_of_journey_pattern import TypeOfJourneyPattern
from .type_of_line import TypeOfLine
from .type_of_link import TypeOfLink
from .type_of_link_sequence import TypeOfLinkSequence
from .type_of_mobility_service import TypeOfMobilityService
from .type_of_mode_of_operation import TypeOfModeOfOperation
from .type_of_notice import TypeOfNotice
from .type_of_operation import TypeOfOperation
from .type_of_organisation import TypeOfOrganisation
from .type_of_organisation_part import TypeOfOrganisationPart
from .type_of_passenger_information_equipment import (
    TypeOfPassengerInformationEquipment,
)
from .type_of_place import TypeOfPlace
from .type_of_plug import TypeOfPlug
from .type_of_point import TypeOfPoint
from .type_of_projection import TypeOfProjection
from .type_of_responsibility_role import TypeOfResponsibilityRole
from .type_of_retail_device import TypeOfRetailDevice
from .type_of_sales_offer_package import TypeOfSalesOfferPackage
from .type_of_service import TypeOfService
from .type_of_tariff import TypeOfTariff
from .type_of_time_demand_type import TypeOfTimeDemandType
from .type_of_transfer import TypeOfTransfer
from .type_of_travel_document import TypeOfTravelDocument
from .type_of_value_version_structure import TypeOfValueVersionStructure
from .type_of_zone import TypeOfZone
from .types_of_frame_rel_structure import TypeOfFrame

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PurposeOfGroupingValueStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "PurposeOfGrouping_ValueStructure"

    classes: None | ClassRefsRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_entity: (
        None
        | TypeOfMobilityService
        | TypeOfRetailDevice
        | CustomerAccountStatus
        | TypeOfCustomerAccount
        | TypeOfFareContractEntry
        | TypeOfFareContract
        | TypeOfTravelDocument
        | TypeOfSalesOfferPackage
        | TypeOfFareProduct
        | TypeOfFareStructureElement
        | TypeOfTariff
        | TypeOfAccessRightAssignment
        | TypeOfFareStructureFactor
        | TypeOfFlexibleService
        | TypeOfTimeDemandType
        | TypeOfPassengerInformationEquipment
        | TypeOfJourneyPattern
        | TypeOfActivation
        | TypeOfModeOfOperation
        | TypeOfPlug
        | TypeOfBatteryChemistry
        | TypeOfLine
        | TypeOfDeliveryVariant
        | TypeOfNotice
        | TypeOfCongestion
        | TypeOfFacility
        | TypeOfService
        | TypeOfEquipment
        | TypeOfFeature
        | TypeOfLinkSequence
        | TypeOfPlace
        | TypeOfTransfer
        | TypeOfOperation
        | TypeOfOrganisationPart
        | TypeOfOrganisation
        | TypeOfZone
        | TypeOfLink
        | TypeOfPoint
        | TypeOfProjection
        | TypeOfFrame
        | TypeOfResponsibilityRole
        | TypeOfEntity
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TypeOfMobilityService",
                    "type": TypeOfMobilityService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfRetailDevice",
                    "type": TypeOfRetailDevice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerAccountStatus",
                    "type": CustomerAccountStatus,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfCustomerAccount",
                    "type": TypeOfCustomerAccount,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareContractEntry",
                    "type": TypeOfFareContractEntry,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareContract",
                    "type": TypeOfFareContract,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTravelDocument",
                    "type": TypeOfTravelDocument,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfSalesOfferPackage",
                    "type": TypeOfSalesOfferPackage,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareProduct",
                    "type": TypeOfFareProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareStructureElement",
                    "type": TypeOfFareStructureElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTariff",
                    "type": TypeOfTariff,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfAccessRightAssignment",
                    "type": TypeOfAccessRightAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareStructureFactor",
                    "type": TypeOfFareStructureFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFlexibleService",
                    "type": TypeOfFlexibleService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTimeDemandType",
                    "type": TypeOfTimeDemandType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPassengerInformationEquipment",
                    "type": TypeOfPassengerInformationEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfJourneyPattern",
                    "type": TypeOfJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfActivation",
                    "type": TypeOfActivation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfModeOfOperation",
                    "type": TypeOfModeOfOperation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPlug",
                    "type": TypeOfPlug,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfBatteryChemistry",
                    "type": TypeOfBatteryChemistry,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfLine",
                    "type": TypeOfLine,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfDeliveryVariant",
                    "type": TypeOfDeliveryVariant,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfNotice",
                    "type": TypeOfNotice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfCongestion",
                    "type": TypeOfCongestion,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFacility",
                    "type": TypeOfFacility,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfService",
                    "type": TypeOfService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfEquipment",
                    "type": TypeOfEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFeature",
                    "type": TypeOfFeature,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfLinkSequence",
                    "type": TypeOfLinkSequence,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPlace",
                    "type": TypeOfPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTransfer",
                    "type": TypeOfTransfer,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfOperation",
                    "type": TypeOfOperation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfOrganisationPart",
                    "type": TypeOfOrganisationPart,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfOrganisation",
                    "type": TypeOfOrganisation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfZone",
                    "type": TypeOfZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfLink",
                    "type": TypeOfLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPoint",
                    "type": TypeOfPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfProjection",
                    "type": TypeOfProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFrame",
                    "type": TypeOfFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfResponsibilityRole",
                    "type": TypeOfResponsibilityRole,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfEntity",
                    "type": TypeOfEntity,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
