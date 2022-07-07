from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    Language,
    ListOfDimension,
    Party,
    Quantity,
    Reference,
    Transport,
)
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
    MaxBackOrderQuantity,
    ParentItemNumber,
    TotalQuantity,
)
from xcbl.models.order_status_result import (
    ErrorInfo,
    LineItemAttachment,
    ResultListOfAttachment,
)
from xcbl.models.payment_request_acknowledgment import SupplierParty


@dataclass
class AvailabilityCheckResultId:
    class Meta:
        name = "AvailabilityCheckResultID"

    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AvailabilityCheckResultLanguage:
    language: Optional[Language] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AvailabilityErrorInfo:
    error_info: Optional[ErrorInfo] = field(
        default=None,
        metadata={
            "name": "ErrorInfo",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AvailabilityShipToParty:
    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AvailableQuantity:
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class CheckResultTransport:
    transport: Optional[Transport] = field(
        default=None,
        metadata={
            "name": "Transport",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SummaryErrorInfo:
    error_info: Optional[ErrorInfo] = field(
        default=None,
        metadata={
            "name": "ErrorInfo",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AvailabilityCheckResultHeader:
    availability_check_result_id: Optional[AvailabilityCheckResultId] = field(
        default=None,
        metadata={
            "name": "AvailabilityCheckResultID",
            "type": "Element",
            "required": True,
        }
    )
    availability_check_result_issue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "AvailabilityCheckResultIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    supplier_party: Optional[SupplierParty] = field(
        default=None,
        metadata={
            "name": "SupplierParty",
            "type": "Element",
            "required": True,
        }
    )
    supplier_idreference_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierIDReferenceDate",
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
    buyer_idreference_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "BuyerIDReferenceDate",
            "type": "Element",
        }
    )
    availability_ship_to_party: Optional[AvailabilityShipToParty] = field(
        default=None,
        metadata={
            "name": "AvailabilityShipToParty",
            "type": "Element",
            "required": True,
        }
    )
    availability_check_result_language: Optional[AvailabilityCheckResultLanguage] = field(
        default=None,
        metadata={
            "name": "AvailabilityCheckResultLanguage",
            "type": "Element",
        }
    )
    availability_check_result_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "AvailabilityCheckResultNote",
            "type": "Element",
        }
    )
    result_list_of_attachment: Optional[ResultListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ResultListOfAttachment",
            "type": "Element",
        }
    )


@dataclass
class AvailabilityCheckResultSummary:
    availability_item_errors: Optional[str] = field(
        default=None,
        metadata={
            "name": "AvailabilityItemErrors",
            "type": "Element",
            "required": True,
        }
    )
    summary_error_info: Optional[SummaryErrorInfo] = field(
        default=None,
        metadata={
            "name": "SummaryErrorInfo",
            "type": "Element",
        }
    )
    total_number_of_line_item: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalNumberOfLineItem",
            "type": "Element",
        }
    )


@dataclass
class CheckResultBaseItemDetail:
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
    check_result_transport: List[CheckResultTransport] = field(
        default_factory=list,
        metadata={
            "name": "CheckResultTransport",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class QuotedItem:
    check_result_base_item_detail: Optional[CheckResultBaseItemDetail] = field(
        default=None,
        metadata={
            "name": "CheckResultBaseItemDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AvailabilityCheckResultItemDetail:
    quoted_item: Optional[QuotedItem] = field(
        default=None,
        metadata={
            "name": "QuotedItem",
            "type": "Element",
            "required": True,
        }
    )
    available_quantity: Optional[AvailableQuantity] = field(
        default=None,
        metadata={
            "name": "AvailableQuantity",
            "type": "Element",
            "required": True,
        }
    )
    delivery_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "DeliveryDate",
            "type": "Element",
        }
    )
    availability_error_info: Optional[AvailabilityErrorInfo] = field(
        default=None,
        metadata={
            "name": "AvailabilityErrorInfo",
            "type": "Element",
        }
    )
    general_line_item_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeneralLineItemNote",
            "type": "Element",
        }
    )
    line_item_attachment: Optional[LineItemAttachment] = field(
        default=None,
        metadata={
            "name": "LineItemAttachment",
            "type": "Element",
        }
    )


@dataclass
class ListOfAvailabilityCheckResultItemDetail:
    availability_check_result_item_detail: List[AvailabilityCheckResultItemDetail] = field(
        default_factory=list,
        metadata={
            "name": "AvailabilityCheckResultItemDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class AvailabilityCheckResultDetail:
    list_of_availability_check_result_item_detail: Optional[ListOfAvailabilityCheckResultItemDetail] = field(
        default=None,
        metadata={
            "name": "ListOfAvailabilityCheckResultItemDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AvailabilityCheckResult:
    availability_check_result_header: Optional[AvailabilityCheckResultHeader] = field(
        default=None,
        metadata={
            "name": "AvailabilityCheckResultHeader",
            "type": "Element",
            "required": True,
        }
    )
    availability_check_result_detail: Optional[AvailabilityCheckResultDetail] = field(
        default=None,
        metadata={
            "name": "AvailabilityCheckResultDetail",
            "type": "Element",
        }
    )
    availability_check_result_summary: Optional[AvailabilityCheckResultSummary] = field(
        default=None,
        metadata={
            "name": "AvailabilityCheckResultSummary",
            "type": "Element",
        }
    )
