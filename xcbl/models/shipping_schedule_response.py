from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    ItemPackagingReference,
    Language,
    ListOfAttachment,
    ListOfContact,
    ListOfDimension,
    ListOfReferenceCoded,
    Location,
    Purpose,
    TermsOfDelivery,
    ValidityDates,
)
from xcbl.models.goods_receipt import ListOfTransportRouting
from xcbl.models.order_request import (
    BuyerParty,
    CatalogReference,
    ConditionsOfSale,
    CountryOfDestination,
    CountryOfOrigin,
    FinalRecipient,
    HazardousMaterials,
    ItemContractReferences,
    ItemIdentifiers,
    LineItemNum,
    LineItemType,
    ListOfItemReferences,
    ListOfPartyCoded,
    ListOfQuantityCoded,
    ListOfStructuredNote,
    MaxBackOrderQuantity,
    ParentItemNumber,
    RequestedResponse,
    SellerParty,
    TotalQuantity,
)
from xcbl.models.planning_schedule import (
    ItemQuantities,
    ItemResourceAuthorization,
    ItemScheduleReference,
    ScheduleDates,
    ScheduleParty,
    SchedulePurpose,
    ScheduleQuantities,
    ScheduleReferences,
)
from xcbl.models.planning_schedule_response import (
    ResponseType,
    ScheduleReference,
)


@dataclass
class ShippingScheduleSummary:
    total_number_of_line_items: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalNumberOfLineItems",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class BaseShippingDetail:
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
    item_packaging_reference: List[ItemPackagingReference] = field(
        default_factory=list,
        metadata={
            "name": "ItemPackagingReference",
            "type": "Element",
        }
    )


@dataclass
class ShipScheduleDetail:
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
    route_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RouteID",
            "type": "Element",
        }
    )


@dataclass
class ShippingScheduleHeader:
    schedule_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ScheduleID",
            "type": "Element",
            "required": True,
        }
    )
    schedule_issued_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "ScheduleIssuedDate",
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
    list_of_transport_routing: Optional[ListOfTransportRouting] = field(
        default=None,
        metadata={
            "name": "ListOfTransportRouting",
            "type": "Element",
        }
    )
    terms_of_delivery: Optional[TermsOfDelivery] = field(
        default=None,
        metadata={
            "name": "TermsOfDelivery",
            "type": "Element",
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
    shipping_schedule_header_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShippingScheduleHeaderNote",
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
class ShippingScheduleResponseSummary:
    shipping_schedule_summary: Optional[ShippingScheduleSummary] = field(
        default=None,
        metadata={
            "name": "ShippingScheduleSummary",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ChangedShippingScheduleHeader:
    shipping_schedule_header: Optional[ShippingScheduleHeader] = field(
        default=None,
        metadata={
            "name": "ShippingScheduleHeader",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfShipScheduleDetail:
    ship_schedule_detail: List[ShipScheduleDetail] = field(
        default_factory=list,
        metadata={
            "name": "ShipScheduleDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class OriginalShippingScheduleHeader:
    shipping_schedule_header: Optional[ShippingScheduleHeader] = field(
        default=None,
        metadata={
            "name": "ShippingScheduleHeader",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class LocationShipSchedule:
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
    list_of_ship_schedule_detail: Optional[ListOfShipScheduleDetail] = field(
        default=None,
        metadata={
            "name": "ListOfShipScheduleDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class LocationShippingItemDetail:
    base_shipping_detail: Optional[BaseShippingDetail] = field(
        default=None,
        metadata={
            "name": "BaseShippingDetail",
            "type": "Element",
            "required": True,
        }
    )
    list_of_ship_schedule_detail: Optional[ListOfShipScheduleDetail] = field(
        default=None,
        metadata={
            "name": "ListOfShipScheduleDetail",
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
class ShippingScheduleResponseHeader:
    schedule_response_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ScheduleResponseID",
            "type": "Element",
            "required": True,
        }
    )
    schedule_response_issue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "ScheduleResponseIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    schedule_reference: Optional[ScheduleReference] = field(
        default=None,
        metadata={
            "name": "ScheduleReference",
            "type": "Element",
            "required": True,
        }
    )
    list_of_reference_coded: Optional[ListOfReferenceCoded] = field(
        default=None,
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
        }
    )
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
    purpose: Optional[Purpose] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Element",
            "required": True,
        }
    )
    response_type: Optional[ResponseType] = field(
        default=None,
        metadata={
            "name": "ResponseType",
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
    original_shipping_schedule_header: Optional[OriginalShippingScheduleHeader] = field(
        default=None,
        metadata={
            "name": "OriginalShippingScheduleHeader",
            "type": "Element",
        }
    )
    changed_shipping_schedule_header: Optional[ChangedShippingScheduleHeader] = field(
        default=None,
        metadata={
            "name": "ChangedShippingScheduleHeader",
            "type": "Element",
        }
    )
    shipping_schedule_response_header_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShippingScheduleResponseHeaderNote",
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
class ListOfLocationShipSchedule:
    location_ship_schedule: List[LocationShipSchedule] = field(
        default_factory=list,
        metadata={
            "name": "LocationShipSchedule",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ListOfLocationShippingItemDetail:
    location_shipping_item_detail: List[LocationShippingItemDetail] = field(
        default_factory=list,
        metadata={
            "name": "LocationShippingItemDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class LocationGroupedShippingDetail:
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
    list_of_location_shipping_item_detail: Optional[ListOfLocationShippingItemDetail] = field(
        default=None,
        metadata={
            "name": "ListOfLocationShippingItemDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class MaterialGroupedShippingDetail:
    base_shipping_detail: Optional[BaseShippingDetail] = field(
        default=None,
        metadata={
            "name": "BaseShippingDetail",
            "type": "Element",
            "required": True,
        }
    )
    list_of_location_ship_schedule: Optional[ListOfLocationShipSchedule] = field(
        default=None,
        metadata={
            "name": "ListOfLocationShipSchedule",
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
class ChangedLocationGroupedShippingDetail:
    location_grouped_shipping_detail: Optional[LocationGroupedShippingDetail] = field(
        default=None,
        metadata={
            "name": "LocationGroupedShippingDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ChangedMaterialGroupedShippingDetail:
    material_grouped_shipping_detail: Optional[MaterialGroupedShippingDetail] = field(
        default=None,
        metadata={
            "name": "MaterialGroupedShippingDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OriginalLocationGroupedShippingDetail:
    location_grouped_shipping_detail: Optional[LocationGroupedShippingDetail] = field(
        default=None,
        metadata={
            "name": "LocationGroupedShippingDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OriginalMaterialGroupedShippingDetail:
    material_grouped_shipping_detail: Optional[MaterialGroupedShippingDetail] = field(
        default=None,
        metadata={
            "name": "MaterialGroupedShippingDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class LocationGroupedShippingResponse:
    detail_response_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "DetailResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    detail_response_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "DetailResponseCodedOther",
            "type": "Element",
        }
    )
    original_location_grouped_shipping_detail: Optional[OriginalLocationGroupedShippingDetail] = field(
        default=None,
        metadata={
            "name": "OriginalLocationGroupedShippingDetail",
            "type": "Element",
        }
    )
    changed_location_grouped_shipping_detail: Optional[ChangedLocationGroupedShippingDetail] = field(
        default=None,
        metadata={
            "name": "ChangedLocationGroupedShippingDetail",
            "type": "Element",
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
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
        }
    )


@dataclass
class MaterialGroupedShippingResponse:
    detail_response_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "DetailResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    detail_response_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "DetailResponseCodedOther",
            "type": "Element",
        }
    )
    original_material_grouped_shipping_detail: Optional[OriginalMaterialGroupedShippingDetail] = field(
        default=None,
        metadata={
            "name": "OriginalMaterialGroupedShippingDetail",
            "type": "Element",
        }
    )
    changed_material_grouped_shipping_detail: Optional[ChangedMaterialGroupedShippingDetail] = field(
        default=None,
        metadata={
            "name": "ChangedMaterialGroupedShippingDetail",
            "type": "Element",
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
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
        }
    )


@dataclass
class ListOfLocationGroupedShippingResponse:
    location_grouped_shipping_response: List[LocationGroupedShippingResponse] = field(
        default_factory=list,
        metadata={
            "name": "LocationGroupedShippingResponse",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ListOfMaterialGroupedShippingResponse:
    material_grouped_shipping_response: List[MaterialGroupedShippingResponse] = field(
        default_factory=list,
        metadata={
            "name": "MaterialGroupedShippingResponse",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ShippingScheduleResponse:
    shipping_schedule_response_header: Optional[ShippingScheduleResponseHeader] = field(
        default=None,
        metadata={
            "name": "ShippingScheduleResponseHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_location_grouped_shipping_response: Optional[ListOfLocationGroupedShippingResponse] = field(
        default=None,
        metadata={
            "name": "ListOfLocationGroupedShippingResponse",
            "type": "Element",
            "required": True,
        }
    )
    list_of_material_grouped_shipping_response: Optional[ListOfMaterialGroupedShippingResponse] = field(
        default=None,
        metadata={
            "name": "ListOfMaterialGroupedShippingResponse",
            "type": "Element",
            "required": True,
        }
    )
    shipping_schedule_response_summary: Optional[ShippingScheduleResponseSummary] = field(
        default=None,
        metadata={
            "name": "ShippingScheduleResponseSummary",
            "type": "Element",
        }
    )
