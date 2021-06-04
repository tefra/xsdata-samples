from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.class_refs_rel_structure import ClassRefsRelStructure
from netex.models.customer_account_status import CustomerAccountStatus
from netex.models.type_of_access_right_assignment import TypeOfAccessRightAssignment
from netex.models.type_of_activation import TypeOfActivation
from netex.models.type_of_congestion import TypeOfCongestion
from netex.models.type_of_customer_account import TypeOfCustomerAccount
from netex.models.type_of_delivery_variant import TypeOfDeliveryVariant
from netex.models.type_of_entity import TypeOfEntity
from netex.models.type_of_equipment import TypeOfEquipment
from netex.models.type_of_facility import TypeOfFacility
from netex.models.type_of_fare_contract import TypeOfFareContract
from netex.models.type_of_fare_contract_entry import TypeOfFareContractEntry
from netex.models.type_of_fare_product import TypeOfFareProduct
from netex.models.type_of_fare_structure_element import TypeOfFareStructureElement
from netex.models.type_of_fare_structure_factor import TypeOfFareStructureFactor
from netex.models.type_of_feature import TypeOfFeature
from netex.models.type_of_flexible_service import TypeOfFlexibleService
from netex.models.type_of_journey_pattern import TypeOfJourneyPattern
from netex.models.type_of_line import TypeOfLine
from netex.models.type_of_link import TypeOfLink
from netex.models.type_of_link_sequence import TypeOfLinkSequence
from netex.models.type_of_notice import TypeOfNotice
from netex.models.type_of_operation import TypeOfOperation
from netex.models.type_of_organisation import TypeOfOrganisation
from netex.models.type_of_organisation_part import TypeOfOrganisationPart
from netex.models.type_of_passenger_information_equipment import TypeOfPassengerInformationEquipment
from netex.models.type_of_place import TypeOfPlace
from netex.models.type_of_point import TypeOfPoint
from netex.models.type_of_projection import TypeOfProjection
from netex.models.type_of_responsibility_role import TypeOfResponsibilityRole
from netex.models.type_of_retail_device import TypeOfRetailDevice
from netex.models.type_of_sales_offer_package import TypeOfSalesOfferPackage
from netex.models.type_of_service import TypeOfService
from netex.models.type_of_tariff import TypeOfTariff
from netex.models.type_of_time_demand_type import TypeOfTimeDemandType
from netex.models.type_of_transfer import TypeOfTransfer
from netex.models.type_of_travel_document import TypeOfTravelDocument
from netex.models.type_of_value_version_structure import TypeOfValueVersionStructure
from netex.models.type_of_zone import TypeOfZone
from netex.models.types_of_frame_rel_structure import TypeOfFrame

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
    type_of_retail_device: List[TypeOfRetailDevice] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfRetailDevice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    customer_account_status: List[CustomerAccountStatus] = field(
        default_factory=list,
        metadata={
            "name": "CustomerAccountStatus",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_customer_account: List[TypeOfCustomerAccount] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfCustomerAccount",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_fare_contract_entry: List[TypeOfFareContractEntry] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareContractEntry",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_fare_contract: List[TypeOfFareContract] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareContract",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_travel_document: List[TypeOfTravelDocument] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfTravelDocument",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_sales_offer_package: List[TypeOfSalesOfferPackage] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfSalesOfferPackage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_fare_product: List[TypeOfFareProduct] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_fare_structure_element: List[TypeOfFareStructureElement] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareStructureElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_tariff: List[TypeOfTariff] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfTariff",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_access_right_assignment: List[TypeOfAccessRightAssignment] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfAccessRightAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_fare_structure_factor: List[TypeOfFareStructureFactor] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareStructureFactor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_flexible_service: List[TypeOfFlexibleService] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFlexibleService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_time_demand_type: List[TypeOfTimeDemandType] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfTimeDemandType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_passenger_information_equipment: List[TypeOfPassengerInformationEquipment] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPassengerInformationEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_congestion: List[TypeOfCongestion] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfCongestion",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_journey_pattern: List[TypeOfJourneyPattern] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfJourneyPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_line: List[TypeOfLine] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfLine",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_activation: List[TypeOfActivation] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfActivation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_delivery_variant: List[TypeOfDeliveryVariant] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfDeliveryVariant",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_notice: List[TypeOfNotice] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfNotice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_facility: List[TypeOfFacility] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFacility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_service: List[TypeOfService] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_equipment: List[TypeOfEquipment] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_feature: List[TypeOfFeature] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFeature",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_link_sequence: List[TypeOfLinkSequence] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfLinkSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_place: List[TypeOfPlace] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_transfer: List[TypeOfTransfer] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfTransfer",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_operation: List[TypeOfOperation] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfOperation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_organisation_part: List[TypeOfOrganisationPart] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfOrganisationPart",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_organisation: List[TypeOfOrganisation] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfOrganisation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_zone: List[TypeOfZone] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_link: List[TypeOfLink] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_point: List[TypeOfPoint] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_projection: List[TypeOfProjection] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfProjection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_frame: List[TypeOfFrame] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFrame",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    type_of_responsibility_role: List[TypeOfResponsibilityRole] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfResponsibilityRole",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
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
