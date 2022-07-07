from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    Language,
    ListOfAttachment,
    ListOfDimension,
    ListOfReferenceCoded,
    ListOfStatusReason,
    Quantity,
    Reference,
    Transport,
)
from xcbl.models.order_request import (
    AccountCode,
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
from xcbl.models.request_for_quotation import OrderParty


@dataclass
class ListOfParameter:
    parameter: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Severity:
    severity_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeverityCoded",
            "type": "Element",
            "required": True,
        }
    )
    severity_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeverityCodedOther",
            "type": "Element",
        }
    )


@dataclass
class StatusEvent:
    status_event_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "StatusEventCoded",
            "type": "Element",
            "required": True,
        }
    )
    status_event_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "StatusEventCodedOther",
            "type": "Element",
        }
    )


@dataclass
class BuyerReferenceNumber:
    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ItemStatusQuantity:
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class LanguageString:
    lang_string: Optional[str] = field(
        default=None,
        metadata={
            "name": "LangString",
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


@dataclass
class LineItemAttachment:
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OrderStatusId:
    class Meta:
        name = "OrderStatusID"

    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OrderStatusItemResultTransport:
    transport: Optional[Transport] = field(
        default=None,
        metadata={
            "name": "Transport",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OrderStatusResultLanguage:
    language: Optional[Language] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OrderStatusResultParty:
    order_party: Optional[OrderParty] = field(
        default=None,
        metadata={
            "name": "OrderParty",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OtherReference:
    list_of_reference_coded: Optional[ListOfReferenceCoded] = field(
        default=None,
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ResultListOfAttachment:
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SellerReferenceNumber:
    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class VarianceQty:
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class CompletionMsg:
    language_string: Optional[LanguageString] = field(
        default=None,
        metadata={
            "name": "LanguageString",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OrderStatusResultHeader:
    order_status_id: Optional[OrderStatusId] = field(
        default=None,
        metadata={
            "name": "OrderStatusID",
            "type": "Element",
            "required": True,
        }
    )
    order_status_issue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderStatusIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    order_status_result_party: Optional[OrderStatusResultParty] = field(
        default=None,
        metadata={
            "name": "OrderStatusResultParty",
            "type": "Element",
            "required": True,
        }
    )
    order_status_result_language: Optional[OrderStatusResultLanguage] = field(
        default=None,
        metadata={
            "name": "OrderStatusResultLanguage",
            "type": "Element",
        }
    )
    order_status_result_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderStatusResultNote",
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
class ErrorInfo:
    completion_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "CompletionText",
            "type": "Element",
            "required": True,
        }
    )
    completion_msg: Optional[CompletionMsg] = field(
        default=None,
        metadata={
            "name": "CompletionMsg",
            "type": "Element",
            "required": True,
        }
    )
    severity: Optional[Severity] = field(
        default=None,
        metadata={
            "name": "Severity",
            "type": "Element",
            "required": True,
        }
    )
    list_of_parameter: Optional[ListOfParameter] = field(
        default=None,
        metadata={
            "name": "ListOfParameter",
            "type": "Element",
        }
    )
    min_retry_secs: Optional[str] = field(
        default=None,
        metadata={
            "name": "MinRetrySecs",
            "type": "Element",
        }
    )
    sw_vendor_error_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SwVendorErrorRef",
            "type": "Element",
        }
    )


@dataclass
class OrderStatusSummaryErrorInfo:
    error_info: Optional[ErrorInfo] = field(
        default=None,
        metadata={
            "name": "ErrorInfo",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ShipmentStatusEvent:
    status_event: Optional[StatusEvent] = field(
        default=None,
        metadata={
            "name": "StatusEvent",
            "type": "Element",
            "required": True,
        }
    )
    list_of_status_reason: Optional[ListOfStatusReason] = field(
        default=None,
        metadata={
            "name": "ListOfStatusReason",
            "type": "Element",
        }
    )
    status_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "StatusNote",
            "type": "Element",
        }
    )
    error_info: Optional[ErrorInfo] = field(
        default=None,
        metadata={
            "name": "ErrorInfo",
            "type": "Element",
        }
    )
    ship_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShipDate",
            "type": "Element",
        }
    )


@dataclass
class Status:
    status_event: Optional[StatusEvent] = field(
        default=None,
        metadata={
            "name": "StatusEvent",
            "type": "Element",
            "required": True,
        }
    )
    list_of_status_reason: Optional[ListOfStatusReason] = field(
        default=None,
        metadata={
            "name": "ListOfStatusReason",
            "type": "Element",
        }
    )
    status_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "StatusNote",
            "type": "Element",
        }
    )
    error_info: Optional[ErrorInfo] = field(
        default=None,
        metadata={
            "name": "ErrorInfo",
            "type": "Element",
        }
    )


@dataclass
class ItemStatusEvent:
    status: Optional[Status] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OrderStatus:
    status: Optional[Status] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OrderStatusResultSummary:
    order_status_check_item_error: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderStatusCheckItemError",
            "type": "Element",
            "required": True,
        }
    )
    order_status_summary_error_info: Optional[OrderStatusSummaryErrorInfo] = field(
        default=None,
        metadata={
            "name": "OrderStatusSummaryErrorInfo",
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
class PaymentStatusEvent:
    status: Optional[Status] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ItemStatus:
    item_status_quantity: Optional[ItemStatusQuantity] = field(
        default=None,
        metadata={
            "name": "ItemStatusQuantity",
            "type": "Element",
            "required": True,
        }
    )
    item_status_event: Optional[ItemStatusEvent] = field(
        default=None,
        metadata={
            "name": "ItemStatusEvent",
            "type": "Element",
            "required": True,
        }
    )
    payment_status_event: Optional[PaymentStatusEvent] = field(
        default=None,
        metadata={
            "name": "PaymentStatusEvent",
            "type": "Element",
        }
    )
    shipment_status_event: Optional[ShipmentStatusEvent] = field(
        default=None,
        metadata={
            "name": "ShipmentStatusEvent",
            "type": "Element",
        }
    )


@dataclass
class OrderStatusResultItem:
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
    order_status_item_result_transport: Optional[OrderStatusItemResultTransport] = field(
        default=None,
        metadata={
            "name": "OrderStatusItemResultTransport",
            "type": "Element",
        }
    )
    variance_qty: Optional[VarianceQty] = field(
        default=None,
        metadata={
            "name": "VarianceQty",
            "type": "Element",
            "required": True,
        }
    )
    item_status: List[ItemStatus] = field(
        default_factory=list,
        metadata={
            "name": "ItemStatus",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ListOfOrderStatusResultItem:
    order_status_result_item: List[OrderStatusResultItem] = field(
        default_factory=list,
        metadata={
            "name": "OrderStatusResultItem",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class OrderStatusResultReference:
    account_code: Optional[AccountCode] = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Element",
        }
    )
    buyer_reference_number: Optional[BuyerReferenceNumber] = field(
        default=None,
        metadata={
            "name": "BuyerReferenceNumber",
            "type": "Element",
            "required": True,
        }
    )
    seller_reference_number: Optional[SellerReferenceNumber] = field(
        default=None,
        metadata={
            "name": "SellerReferenceNumber",
            "type": "Element",
            "required": True,
        }
    )
    other_reference: Optional[OtherReference] = field(
        default=None,
        metadata={
            "name": "OtherReference",
            "type": "Element",
        }
    )
    order_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderDate",
            "type": "Element",
            "required": True,
        }
    )
    order_status_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderStatusDate",
            "type": "Element",
            "required": True,
        }
    )
    order_status: Optional[OrderStatus] = field(
        default=None,
        metadata={
            "name": "OrderStatus",
            "type": "Element",
            "required": True,
        }
    )
    payment_status_event: Optional[PaymentStatusEvent] = field(
        default=None,
        metadata={
            "name": "PaymentStatusEvent",
            "type": "Element",
        }
    )
    shipment_status_event: Optional[ShipmentStatusEvent] = field(
        default=None,
        metadata={
            "name": "ShipmentStatusEvent",
            "type": "Element",
        }
    )
    list_of_order_status_result_item: Optional[ListOfOrderStatusResultItem] = field(
        default=None,
        metadata={
            "name": "ListOfOrderStatusResultItem",
            "type": "Element",
        }
    )


@dataclass
class OrderStatusDetailResult:
    order_status_result_reference: Optional[OrderStatusResultReference] = field(
        default=None,
        metadata={
            "name": "OrderStatusResultReference",
            "type": "Element",
            "required": True,
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
class ListOfOrderStatusResultDetail:
    order_status_detail_result: List[OrderStatusDetailResult] = field(
        default_factory=list,
        metadata={
            "name": "OrderStatusDetailResult",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class OrderStatusResultDetail:
    list_of_order_status_result_detail: Optional[ListOfOrderStatusResultDetail] = field(
        default=None,
        metadata={
            "name": "ListOfOrderStatusResultDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OrderStatusResult:
    order_status_result_header: Optional[OrderStatusResultHeader] = field(
        default=None,
        metadata={
            "name": "OrderStatusResultHeader",
            "type": "Element",
            "required": True,
        }
    )
    order_status_result_detail: Optional[OrderStatusResultDetail] = field(
        default=None,
        metadata={
            "name": "OrderStatusResultDetail",
            "type": "Element",
        }
    )
    order_status_result_summary: Optional[OrderStatusResultSummary] = field(
        default=None,
        metadata={
            "name": "OrderStatusResultSummary",
            "type": "Element",
        }
    )
