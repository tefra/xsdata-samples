from dataclasses import dataclass, field
from typing import Optional
from .class_refs_rel_structure import ClassRefsRelStructure
from .customer_account_status import CustomerAccountStatus
from .type_of_access_right_assignment import TypeOfAccessRightAssignment
from .type_of_activation import TypeOfActivation
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
from .type_of_notice import TypeOfNotice
from .type_of_operation import TypeOfOperation
from .type_of_organisation import TypeOfOrganisation
from .type_of_organisation_part import TypeOfOrganisationPart
from .type_of_passenger_information_equipment import TypeOfPassengerInformationEquipment
from .type_of_place import TypeOfPlace
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


@dataclass
class PurposeOfGroupingValueStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "PurposeOfGrouping_ValueStructure"

    classes: Optional[ClassRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_retail_device: Optional[TypeOfRetailDevice] = field(
        default=None,
        metadata={
            "name": "TypeOfRetailDevice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_account_status: Optional[CustomerAccountStatus] = field(
        default=None,
        metadata={
            "name": "CustomerAccountStatus",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_customer_account: Optional[TypeOfCustomerAccount] = field(
        default=None,
        metadata={
            "name": "TypeOfCustomerAccount",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_fare_contract_entry: Optional[TypeOfFareContractEntry] = field(
        default=None,
        metadata={
            "name": "TypeOfFareContractEntry",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_fare_contract: Optional[TypeOfFareContract] = field(
        default=None,
        metadata={
            "name": "TypeOfFareContract",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_travel_document: Optional[TypeOfTravelDocument] = field(
        default=None,
        metadata={
            "name": "TypeOfTravelDocument",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_sales_offer_package: Optional[TypeOfSalesOfferPackage] = field(
        default=None,
        metadata={
            "name": "TypeOfSalesOfferPackage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_fare_product: Optional[TypeOfFareProduct] = field(
        default=None,
        metadata={
            "name": "TypeOfFareProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_fare_structure_element: Optional[TypeOfFareStructureElement] = field(
        default=None,
        metadata={
            "name": "TypeOfFareStructureElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_tariff: Optional[TypeOfTariff] = field(
        default=None,
        metadata={
            "name": "TypeOfTariff",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_access_right_assignment: Optional[TypeOfAccessRightAssignment] = field(
        default=None,
        metadata={
            "name": "TypeOfAccessRightAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_fare_structure_factor: Optional[TypeOfFareStructureFactor] = field(
        default=None,
        metadata={
            "name": "TypeOfFareStructureFactor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_flexible_service: Optional[TypeOfFlexibleService] = field(
        default=None,
        metadata={
            "name": "TypeOfFlexibleService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_time_demand_type: Optional[TypeOfTimeDemandType] = field(
        default=None,
        metadata={
            "name": "TypeOfTimeDemandType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_passenger_information_equipment: Optional[TypeOfPassengerInformationEquipment] = field(
        default=None,
        metadata={
            "name": "TypeOfPassengerInformationEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_congestion: Optional[TypeOfCongestion] = field(
        default=None,
        metadata={
            "name": "TypeOfCongestion",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_journey_pattern: Optional[TypeOfJourneyPattern] = field(
        default=None,
        metadata={
            "name": "TypeOfJourneyPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_line: Optional[TypeOfLine] = field(
        default=None,
        metadata={
            "name": "TypeOfLine",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_activation: Optional[TypeOfActivation] = field(
        default=None,
        metadata={
            "name": "TypeOfActivation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_delivery_variant: Optional[TypeOfDeliveryVariant] = field(
        default=None,
        metadata={
            "name": "TypeOfDeliveryVariant",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_notice: Optional[TypeOfNotice] = field(
        default=None,
        metadata={
            "name": "TypeOfNotice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_facility: Optional[TypeOfFacility] = field(
        default=None,
        metadata={
            "name": "TypeOfFacility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_service: Optional[TypeOfService] = field(
        default=None,
        metadata={
            "name": "TypeOfService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_equipment: Optional[TypeOfEquipment] = field(
        default=None,
        metadata={
            "name": "TypeOfEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_feature: Optional[TypeOfFeature] = field(
        default=None,
        metadata={
            "name": "TypeOfFeature",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_link_sequence: Optional[TypeOfLinkSequence] = field(
        default=None,
        metadata={
            "name": "TypeOfLinkSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_place: Optional[TypeOfPlace] = field(
        default=None,
        metadata={
            "name": "TypeOfPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_transfer: Optional[TypeOfTransfer] = field(
        default=None,
        metadata={
            "name": "TypeOfTransfer",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_operation: Optional[TypeOfOperation] = field(
        default=None,
        metadata={
            "name": "TypeOfOperation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_organisation_part: Optional[TypeOfOrganisationPart] = field(
        default=None,
        metadata={
            "name": "TypeOfOrganisationPart",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_organisation: Optional[TypeOfOrganisation] = field(
        default=None,
        metadata={
            "name": "TypeOfOrganisation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_zone: Optional[TypeOfZone] = field(
        default=None,
        metadata={
            "name": "TypeOfZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_link: Optional[TypeOfLink] = field(
        default=None,
        metadata={
            "name": "TypeOfLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_point: Optional[TypeOfPoint] = field(
        default=None,
        metadata={
            "name": "TypeOfPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_projection: Optional[TypeOfProjection] = field(
        default=None,
        metadata={
            "name": "TypeOfProjection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_frame: Optional[TypeOfFrame] = field(
        default=None,
        metadata={
            "name": "TypeOfFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_responsibility_role: Optional[TypeOfResponsibilityRole] = field(
        default=None,
        metadata={
            "name": "TypeOfResponsibilityRole",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_entity: Optional[TypeOfEntity] = field(
        default=None,
        metadata={
            "name": "TypeOfEntity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
