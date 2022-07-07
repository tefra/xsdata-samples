from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    Language,
    ListOfAttachment,
    ListOfContact,
    ListOfDateCoded,
    ListOfDimension,
    ListOfReferenceCoded,
    Location,
    Party,
    Purpose,
    ValidityDates,
)
from xcbl.models.order_request import (
    BillToParty,
    BuyerParty,
    CatalogReference,
    ConditionsOfSale,
    ContractReferences,
    CountryOfDestination,
    CountryOfOrigin,
    FinalRecipient,
    HazardousMaterials,
    ItemContractReferences,
    ItemIdentifiers,
    LineItemNum,
    LineItemType,
    ListOfItemReferences,
    ListOfMessageId,
    ListOfPartyCoded,
    ListOfQuantityCoded,
    ListOfStructuredNote,
    MaxBackOrderQuantity,
    ParentItemNumber,
    RequestedResponse,
    SellerParty,
    ShipFromParty,
    ShipToParty,
    TotalQuantity,
)


@dataclass
class OrderType:
    order_type_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    order_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderTypeCodedOther",
            "type": "Element",
        }
    )


@dataclass
class PlanningScheduleSummary:
    total_number_of_line_items: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalNumberOfLineItems",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ItemQuantities:
    list_of_quantity_coded: Optional[ListOfQuantityCoded] = field(
        default=None,
        metadata={
            "name": "ListOfQuantityCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ItemResourceAuthorization:
    resource_authorization_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResourceAuthorizationCoded",
            "type": "Element",
            "required": True,
        }
    )
    resource_authorization_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResourceAuthorizationCodedOther",
            "type": "Element",
        }
    )
    validity_dates: Optional[ValidityDates] = field(
        default=None,
        metadata={
            "name": "ValidityDates",
            "type": "Element",
        }
    )


@dataclass
class MaterialIssuerParty:
    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OrderNumber:
    buyer_order_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "BuyerOrderNumber",
            "type": "Element",
            "required": True,
        }
    )
    seller_order_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SellerOrderNumber",
            "type": "Element",
        }
    )
    list_of_message_id: Optional[ListOfMessageId] = field(
        default=None,
        metadata={
            "name": "ListOfMessageID",
            "type": "Element",
        }
    )


@dataclass
class OtherSchedleReferences:
    list_of_reference_coded: Optional[ListOfReferenceCoded] = field(
        default=None,
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ScheduleDates:
    list_of_date_coded: Optional[ListOfDateCoded] = field(
        default=None,
        metadata={
            "name": "ListOfDateCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SchedulePurpose:
    purpose: Optional[Purpose] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ScheduleQuantities:
    list_of_quantity_coded: Optional[ListOfQuantityCoded] = field(
        default=None,
        metadata={
            "name": "ListOfQuantityCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ScheduleDetail:
    commitment_level_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "CommitmentLevelCoded",
            "type": "Element",
            "required": True,
        }
    )
    commitment_level_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "CommitmentLevelCodedOther",
            "type": "Element",
        }
    )
    schedule_dates: Optional[ScheduleDates] = field(
        default=None,
        metadata={
            "name": "ScheduleDates",
            "type": "Element",
            "required": True,
        }
    )
    schedule_quantities: Optional[ScheduleQuantities] = field(
        default=None,
        metadata={
            "name": "ScheduleQuantities",
            "type": "Element",
            "required": True,
        }
    )
    item_resource_authorization: Optional[ItemResourceAuthorization] = field(
        default=None,
        metadata={
            "name": "ItemResourceAuthorization",
            "type": "Element",
        }
    )
    schedule_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "ScheduleNote",
            "type": "Element",
        }
    )


@dataclass
class ScheduleOrderReference:
    order_number: Optional[OrderNumber] = field(
        default=None,
        metadata={
            "name": "OrderNumber",
            "type": "Element",
            "required": True,
        }
    )
    order_issue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderIssueDate",
            "type": "Element",
        }
    )
    order_type: Optional[OrderType] = field(
        default=None,
        metadata={
            "name": "OrderType",
            "type": "Element",
        }
    )


@dataclass
class ScheduleParty:
    buyer_party: Optional[BuyerParty] = field(
        default=None,
        metadata={
            "name": "BuyerParty",
            "type": "Element",
            "required": True,
        }
    )
    seller_party: Optional[SellerParty] = field(
        default=None,
        metadata={
            "name": "SellerParty",
            "type": "Element",
            "required": True,
        }
    )
    ship_from_party: Optional[ShipFromParty] = field(
        default=None,
        metadata={
            "name": "ShipFromParty",
            "type": "Element",
            "required": True,
        }
    )
    ship_to_party: Optional[ShipToParty] = field(
        default=None,
        metadata={
            "name": "ShipToParty",
            "type": "Element",
            "required": True,
        }
    )
    bill_to_party: Optional[BillToParty] = field(
        default=None,
        metadata={
            "name": "BillToParty",
            "type": "Element",
        }
    )
    material_issuer_party: Optional[MaterialIssuerParty] = field(
        default=None,
        metadata={
            "name": "MaterialIssuerParty",
            "type": "Element",
        }
    )
    list_of_party_coded: Optional[ListOfPartyCoded] = field(
        default=None,
        metadata={
            "name": "ListOfPartyCoded",
            "type": "Element",
        }
    )


@dataclass
class ListOfScheduleDetail:
    schedule_detail: List[ScheduleDetail] = field(
        default_factory=list,
        metadata={
            "name": "ScheduleDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ScheduleReferences:
    contract_references: Optional[ContractReferences] = field(
        default=None,
        metadata={
            "name": "ContractReferences",
            "type": "Element",
        }
    )
    schedule_order_reference: Optional[ScheduleOrderReference] = field(
        default=None,
        metadata={
            "name": "ScheduleOrderReference",
            "type": "Element",
        }
    )
    order_type: Optional[OrderType] = field(
        default=None,
        metadata={
            "name": "OrderType",
            "type": "Element",
        }
    )
    other_schedle_references: Optional[OtherSchedleReferences] = field(
        default=None,
        metadata={
            "name": "OtherSchedleReferences",
            "type": "Element",
        }
    )


@dataclass
class ItemScheduleReference:
    schedule_references: Optional[ScheduleReferences] = field(
        default=None,
        metadata={
            "name": "ScheduleReferences",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class LocationSchedule:
    location: Optional[Location] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
        }
    )
    list_of_contact: Optional[ListOfContact] = field(
        default=None,
        metadata={
            "name": "ListOfContact",
            "type": "Element",
        }
    )
    list_of_schedule_detail: Optional[ListOfScheduleDetail] = field(
        default=None,
        metadata={
            "name": "ListOfScheduleDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PlanningScheduleHeader:
    schedule_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ScheduleID",
            "type": "Element",
            "required": True,
        }
    )
    schedule_issue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "ScheduleIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    schedule_references: Optional[ScheduleReferences] = field(
        default=None,
        metadata={
            "name": "ScheduleReferences",
            "type": "Element",
        }
    )
    release_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReleaseNumber",
            "type": "Element",
        }
    )
    schedule_purpose: Optional[SchedulePurpose] = field(
        default=None,
        metadata={
            "name": "SchedulePurpose",
            "type": "Element",
            "required": True,
        }
    )
    requested_response: Optional[RequestedResponse] = field(
        default=None,
        metadata={
            "name": "RequestedResponse",
            "type": "Element",
        }
    )
    schedule_type_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ScheduleTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    schedule_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ScheduleTypeCodedOther",
            "type": "Element",
        }
    )
    quantity_qualifier_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "QuantityQualifierCoded",
            "type": "Element",
            "required": True,
        }
    )
    quantity_qualifier_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "QuantityQualifierCodedOther",
            "type": "Element",
        }
    )
    validity_dates: Optional[ValidityDates] = field(
        default=None,
        metadata={
            "name": "ValidityDates",
            "type": "Element",
        }
    )
    schedule_party: Optional[ScheduleParty] = field(
        default=None,
        metadata={
            "name": "ScheduleParty",
            "type": "Element",
            "required": True,
        }
    )
    language: Optional[Language] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )
    planning_schedule_header_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlanningScheduleHeaderNote",
            "type": "Element",
        }
    )
    list_of_structured_note: Optional[ListOfStructuredNote] = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        }
    )
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
        }
    )


@dataclass
class BasePlanningDetail:
    line_item_num: Optional[LineItemNum] = field(
        default=None,
        metadata={
            "name": "LineItemNum",
            "type": "Element",
            "required": True,
        }
    )
    line_item_type: Optional[LineItemType] = field(
        default=None,
        metadata={
            "name": "LineItemType",
            "type": "Element",
        }
    )
    parent_item_number: Optional[ParentItemNumber] = field(
        default=None,
        metadata={
            "name": "ParentItemNumber",
            "type": "Element",
        }
    )
    item_identifiers: Optional[ItemIdentifiers] = field(
        default=None,
        metadata={
            "name": "ItemIdentifiers",
            "type": "Element",
        }
    )
    list_of_dimension: Optional[ListOfDimension] = field(
        default=None,
        metadata={
            "name": "ListOfDimension",
            "type": "Element",
        }
    )
    total_quantity: Optional[TotalQuantity] = field(
        default=None,
        metadata={
            "name": "TotalQuantity",
            "type": "Element",
        }
    )
    max_back_order_quantity: Optional[MaxBackOrderQuantity] = field(
        default=None,
        metadata={
            "name": "MaxBackOrderQuantity",
            "type": "Element",
        }
    )
    list_of_quantity_coded: Optional[ListOfQuantityCoded] = field(
        default=None,
        metadata={
            "name": "ListOfQuantityCoded",
            "type": "Element",
        }
    )
    off_catalog_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "OffCatalogFlag",
            "type": "Element",
        }
    )
    catalog_reference: Optional[CatalogReference] = field(
        default=None,
        metadata={
            "name": "CatalogReference",
            "type": "Element",
        }
    )
    item_contract_references: Optional[ItemContractReferences] = field(
        default=None,
        metadata={
            "name": "ItemContractReferences",
            "type": "Element",
        }
    )
    list_of_item_references: Optional[ListOfItemReferences] = field(
        default=None,
        metadata={
            "name": "ListOfItemReferences",
            "type": "Element",
        }
    )
    country_of_origin: Optional[CountryOfOrigin] = field(
        default=None,
        metadata={
            "name": "CountryOfOrigin",
            "type": "Element",
        }
    )
    country_of_destination: Optional[CountryOfDestination] = field(
        default=None,
        metadata={
            "name": "CountryOfDestination",
            "type": "Element",
        }
    )
    final_recipient: Optional[FinalRecipient] = field(
        default=None,
        metadata={
            "name": "FinalRecipient",
            "type": "Element",
        }
    )
    list_of_party_coded: Optional[ListOfPartyCoded] = field(
        default=None,
        metadata={
            "name": "ListOfPartyCoded",
            "type": "Element",
        }
    )
    conditions_of_sale: Optional[ConditionsOfSale] = field(
        default=None,
        metadata={
            "name": "ConditionsOfSale",
            "type": "Element",
        }
    )
    hazardous_materials: Optional[HazardousMaterials] = field(
        default=None,
        metadata={
            "name": "HazardousMaterials",
            "type": "Element",
        }
    )
    record_keeping_year: Optional[str] = field(
        default=None,
        metadata={
            "name": "RecordKeepingYear",
            "type": "Element",
        }
    )
    item_schedule_reference: Optional[ItemScheduleReference] = field(
        default=None,
        metadata={
            "name": "ItemScheduleReference",
            "type": "Element",
        }
    )
    forecast_frequency_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ForecastFrequencyCoded",
            "type": "Element",
            "required": True,
        }
    )
    forecast_frequency_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ForecastFrequencyCodedOther",
            "type": "Element",
        }
    )
    item_quantities: Optional[ItemQuantities] = field(
        default=None,
        metadata={
            "name": "ItemQuantities",
            "type": "Element",
        }
    )
    item_release_status_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemReleaseStatusCoded",
            "type": "Element",
        }
    )
    item_release_status_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemReleaseStatusCodedOther",
            "type": "Element",
        }
    )


@dataclass
class ListOfLocationSchedule:
    location_schedule: List[LocationSchedule] = field(
        default_factory=list,
        metadata={
            "name": "LocationSchedule",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class LocationPlanningItemDetail:
    base_planning_detail: Optional[BasePlanningDetail] = field(
        default=None,
        metadata={
            "name": "BasePlanningDetail",
            "type": "Element",
            "required": True,
        }
    )
    list_of_schedule_detail: Optional[ListOfScheduleDetail] = field(
        default=None,
        metadata={
            "name": "ListOfScheduleDetail",
            "type": "Element",
            "required": True,
        }
    )
    line_item_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineItemNote",
            "type": "Element",
        }
    )
    list_of_structured_note: Optional[ListOfStructuredNote] = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        }
    )


@dataclass
class MaterialGroupedPlanningDetail:
    base_planning_detail: Optional[BasePlanningDetail] = field(
        default=None,
        metadata={
            "name": "BasePlanningDetail",
            "type": "Element",
            "required": True,
        }
    )
    list_of_location_schedule: Optional[ListOfLocationSchedule] = field(
        default=None,
        metadata={
            "name": "ListOfLocationSchedule",
            "type": "Element",
            "required": True,
        }
    )
    line_item_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineItemNote",
            "type": "Element",
        }
    )
    list_of_structured_note: Optional[ListOfStructuredNote] = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        }
    )


@dataclass
class ListOfLocationPlanningItemDetail:
    location_planning_item_detail: List[LocationPlanningItemDetail] = field(
        default_factory=list,
        metadata={
            "name": "LocationPlanningItemDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ListOfMaterialGroupedPlanningDetail:
    material_grouped_planning_detail: List[MaterialGroupedPlanningDetail] = field(
        default_factory=list,
        metadata={
            "name": "MaterialGroupedPlanningDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class LocationGroupedPlanningDetail:
    location: Optional[Location] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "required": True,
        }
    )
    list_of_contact: Optional[ListOfContact] = field(
        default=None,
        metadata={
            "name": "ListOfContact",
            "type": "Element",
        }
    )
    list_of_location_planning_item_detail: Optional[ListOfLocationPlanningItemDetail] = field(
        default=None,
        metadata={
            "name": "ListOfLocationPlanningItemDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfLocationGroupedPlanningDetail:
    location_grouped_planning_detail: List[LocationGroupedPlanningDetail] = field(
        default_factory=list,
        metadata={
            "name": "LocationGroupedPlanningDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class PlanningSchedule:
    planning_schedule_header: Optional[PlanningScheduleHeader] = field(
        default=None,
        metadata={
            "name": "PlanningScheduleHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_location_grouped_planning_detail: Optional[ListOfLocationGroupedPlanningDetail] = field(
        default=None,
        metadata={
            "name": "ListOfLocationGroupedPlanningDetail",
            "type": "Element",
            "required": True,
        }
    )
    list_of_material_grouped_planning_detail: Optional[ListOfMaterialGroupedPlanningDetail] = field(
        default=None,
        metadata={
            "name": "ListOfMaterialGroupedPlanningDetail",
            "type": "Element",
            "required": True,
        }
    )
    planning_schedule_summary: Optional[PlanningScheduleSummary] = field(
        default=None,
        metadata={
            "name": "PlanningScheduleSummary",
            "type": "Element",
        }
    )
