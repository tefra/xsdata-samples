from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    Currency,
    Language,
    ListOfReferenceCoded,
    OrderDates,
    Purpose,
    Reference,
)
from xcbl.models.availability_check_result import AvailabilityErrorInfo
from xcbl.models.order_request import (
    BuyerParty,
    ItemDetail,
    ListOfMessageId,
    ListOfNameValueSet,
    ListOfStructuredNote,
    ListOfTransport,
    OrderAllowancesOrCharges,
    OrderHeaderAttachments,
    OrderHeaderPrice,
    OrderPaymentInstructions,
    OrderReferences,
    OrderSummary,
    OrderTermsOfDelivery,
    PackageDetail,
    RequestedResponse,
    RoundTripInformation,
    SellerParty,
    TaxAccountingCurrency,
    TaxReference,
)
from xcbl.models.order_status_result import (
    ErrorInfo,
    ItemStatusEvent,
    OrderStatus,
    PaymentStatusEvent,
    ShipmentStatusEvent,
)
from xcbl.models.planning_schedule import (
    OrderNumber,
    OrderType,
)
from xcbl.models.planning_schedule_response import ResponseType
from xcbl.models.price_check_result import PriceErrorInfo
from xcbl.models.request_for_quotation import OrderParty


@dataclass
class ChangeType:
    change_type_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChangeTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    change_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChangeTypeCodedOther",
            "type": "Element",
        }
    )


@dataclass
class ChangeOrderNumber:
    buyer_change_order_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "BuyerChangeOrderNumber",
            "type": "Element",
            "required": True,
        }
    )
    seller_change_order_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SellerChangeOrderNumber",
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
class ChangeOrderReference:
    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ItemDetailChanges:
    item_detail: Optional[ItemDetail] = field(
        default=None,
        metadata={
            "name": "ItemDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfErrorInfo:
    error_info: List[ErrorInfo] = field(
        default_factory=list,
        metadata={
            "name": "ErrorInfo",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class OrderCurrency:
    currency: Optional[Currency] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OrderLanguage:
    language: Optional[Language] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OrderReference:
    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OrderResponseNumber:
    buyer_order_response_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "BuyerOrderResponseNumber",
            "type": "Element",
            "required": True,
        }
    )
    seller_order_response_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SellerOrderResponseNumber",
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
class OrderTaxReference:
    tax_reference: Optional[TaxReference] = field(
        default=None,
        metadata={
            "name": "TaxReference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OriginalItemDetail:
    item_detail: Optional[ItemDetail] = field(
        default=None,
        metadata={
            "name": "ItemDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OriginalOrderSummary:
    order_summary: Optional[OrderSummary] = field(
        default=None,
        metadata={
            "name": "OrderSummary",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OriginalPackageDetail:
    package_detail: Optional[PackageDetail] = field(
        default=None,
        metadata={
            "name": "PackageDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PackageDetailChanges:
    package_detail: Optional[PackageDetail] = field(
        default=None,
        metadata={
            "name": "PackageDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class RevisedOrderSummary:
    order_summary: Optional[OrderSummary] = field(
        default=None,
        metadata={
            "name": "OrderSummary",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ChangeOrderItemDetail:
    item_detail_change_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemDetailChangeCoded",
            "type": "Element",
            "required": True,
        }
    )
    item_detail_change_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemDetailChangeCodedOther",
            "type": "Element",
        }
    )
    list_of_reference_coded: Optional[ListOfReferenceCoded] = field(
        default=None,
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
        }
    )
    original_item_detail: Optional[OriginalItemDetail] = field(
        default=None,
        metadata={
            "name": "OriginalItemDetail",
            "type": "Element",
        }
    )
    item_detail_changes: Optional[ItemDetailChanges] = field(
        default=None,
        metadata={
            "name": "ItemDetailChanges",
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


@dataclass
class ChangeOrderPackageDetail:
    package_detail_change_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "PackageDetailChangeCoded",
            "type": "Element",
            "required": True,
        }
    )
    package_detail_change_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "PackageDetailChangeCodedOther",
            "type": "Element",
        }
    )
    original_package_detail: Optional[OriginalPackageDetail] = field(
        default=None,
        metadata={
            "name": "OriginalPackageDetail",
            "type": "Element",
        }
    )
    package_detail_changes: Optional[PackageDetailChanges] = field(
        default=None,
        metadata={
            "name": "PackageDetailChanges",
            "type": "Element",
        }
    )
    package_detail_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "PackageDetailNote",
            "type": "Element",
        }
    )


@dataclass
class OrderHeader:
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
            "required": True,
        }
    )
    order_references: Optional[OrderReferences] = field(
        default=None,
        metadata={
            "name": "OrderReferences",
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
    purpose: Optional[Purpose] = field(
        default=None,
        metadata={
            "name": "Purpose",
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
    order_type: Optional[OrderType] = field(
        default=None,
        metadata={
            "name": "OrderType",
            "type": "Element",
        }
    )
    order_currency: Optional[OrderCurrency] = field(
        default=None,
        metadata={
            "name": "OrderCurrency",
            "type": "Element",
            "required": True,
        }
    )
    tax_accounting_currency: Optional[TaxAccountingCurrency] = field(
        default=None,
        metadata={
            "name": "TaxAccountingCurrency",
            "type": "Element",
        }
    )
    order_language: Optional[OrderLanguage] = field(
        default=None,
        metadata={
            "name": "OrderLanguage",
            "type": "Element",
            "required": True,
        }
    )
    order_tax_reference: Optional[OrderTaxReference] = field(
        default=None,
        metadata={
            "name": "OrderTaxReference",
            "type": "Element",
        }
    )
    order_invoice_medium_type_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderInvoiceMediumTypeCoded",
            "type": "Element",
        }
    )
    order_invoice_medium_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderInvoiceMediumTypeCodedOther",
            "type": "Element",
        }
    )
    order_dates: Optional[OrderDates] = field(
        default=None,
        metadata={
            "name": "OrderDates",
            "type": "Element",
        }
    )
    partial_shipment_allowed: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartialShipmentAllowed",
            "type": "Element",
        }
    )
    order_party: Optional[OrderParty] = field(
        default=None,
        metadata={
            "name": "OrderParty",
            "type": "Element",
            "required": True,
        }
    )
    part_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartLocation",
            "type": "Element",
        }
    )
    list_of_transport: Optional[ListOfTransport] = field(
        default=None,
        metadata={
            "name": "ListOfTransport",
            "type": "Element",
        }
    )
    order_terms_of_delivery: List[OrderTermsOfDelivery] = field(
        default_factory=list,
        metadata={
            "name": "OrderTermsOfDelivery",
            "type": "Element",
        }
    )
    order_header_price: Optional[OrderHeaderPrice] = field(
        default=None,
        metadata={
            "name": "OrderHeaderPrice",
            "type": "Element",
        }
    )
    order_payment_instructions: Optional[OrderPaymentInstructions] = field(
        default=None,
        metadata={
            "name": "OrderPaymentInstructions",
            "type": "Element",
        }
    )
    order_allowances_or_charges: Optional[OrderAllowancesOrCharges] = field(
        default=None,
        metadata={
            "name": "OrderAllowancesOrCharges",
            "type": "Element",
        }
    )
    round_trip_information: Optional[RoundTripInformation] = field(
        default=None,
        metadata={
            "name": "RoundTripInformation",
            "type": "Element",
        }
    )
    order_header_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderHeaderNote",
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
    list_of_name_value_set: Optional[ListOfNameValueSet] = field(
        default=None,
        metadata={
            "name": "ListOfNameValueSet",
            "type": "Element",
        }
    )
    order_header_attachments: Optional[OrderHeaderAttachments] = field(
        default=None,
        metadata={
            "name": "OrderHeaderAttachments",
            "type": "Element",
        }
    )


@dataclass
class OrderResponseSummary:
    error_info: Optional[ErrorInfo] = field(
        default=None,
        metadata={
            "name": "ErrorInfo",
            "type": "Element",
        }
    )
    original_order_summary: Optional[OriginalOrderSummary] = field(
        default=None,
        metadata={
            "name": "OriginalOrderSummary",
            "type": "Element",
        }
    )
    revised_order_summary: Optional[RevisedOrderSummary] = field(
        default=None,
        metadata={
            "name": "RevisedOrderSummary",
            "type": "Element",
        }
    )


@dataclass
class OrderHeaderChanges:
    order_header: Optional[OrderHeader] = field(
        default=None,
        metadata={
            "name": "OrderHeader",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OrderResponseItemDetail:
    item_detail_response_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemDetailResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    item_detail_response_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemDetailResponseCodedOther",
            "type": "Element",
        }
    )
    item_status_event: Optional[ItemStatusEvent] = field(
        default=None,
        metadata={
            "name": "ItemStatusEvent",
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
    payment_status_event: Optional[PaymentStatusEvent] = field(
        default=None,
        metadata={
            "name": "PaymentStatusEvent",
            "type": "Element",
        }
    )
    price_error_info: Optional[PriceErrorInfo] = field(
        default=None,
        metadata={
            "name": "PriceErrorInfo",
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
    list_of_error_info: Optional[ListOfErrorInfo] = field(
        default=None,
        metadata={
            "name": "ListOfErrorInfo",
            "type": "Element",
        }
    )
    tracking_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrackingURL",
            "type": "Element",
        }
    )
    list_of_reference_coded: Optional[ListOfReferenceCoded] = field(
        default=None,
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
        }
    )
    original_item_detail: Optional[OriginalItemDetail] = field(
        default=None,
        metadata={
            "name": "OriginalItemDetail",
            "type": "Element",
            "required": True,
        }
    )
    change_order_item_detail: Optional[ChangeOrderItemDetail] = field(
        default=None,
        metadata={
            "name": "ChangeOrderItemDetail",
            "type": "Element",
            "required": True,
        }
    )
    item_detail_changes: Optional[ItemDetailChanges] = field(
        default=None,
        metadata={
            "name": "ItemDetailChanges",
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


@dataclass
class OrderResponsePackageDetail:
    package_detail_response_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "PackageDetailResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    package_detail_response_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "PackageDetailResponseCodedOther",
            "type": "Element",
        }
    )
    original_package_detail: Optional[OriginalPackageDetail] = field(
        default=None,
        metadata={
            "name": "OriginalPackageDetail",
            "type": "Element",
            "required": True,
        }
    )
    change_order_package_detail: Optional[ChangeOrderPackageDetail] = field(
        default=None,
        metadata={
            "name": "ChangeOrderPackageDetail",
            "type": "Element",
            "required": True,
        }
    )
    package_detail_changes: Optional[PackageDetailChanges] = field(
        default=None,
        metadata={
            "name": "PackageDetailChanges",
            "type": "Element",
        }
    )
    package_detail_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "PackageDetailNote",
            "type": "Element",
        }
    )


@dataclass
class OriginalOrderHeader:
    order_header: Optional[OrderHeader] = field(
        default=None,
        metadata={
            "name": "OrderHeader",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ChangeOrderHeader:
    change_order_number: Optional[ChangeOrderNumber] = field(
        default=None,
        metadata={
            "name": "ChangeOrderNumber",
            "type": "Element",
            "required": True,
        }
    )
    change_order_sequence: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChangeOrderSequence",
            "type": "Element",
            "required": True,
        }
    )
    change_order_issue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChangeOrderIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    order_reference: Optional[OrderReference] = field(
        default=None,
        metadata={
            "name": "OrderReference",
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
    buyer_party: Optional[BuyerParty] = field(
        default=None,
        metadata={
            "name": "BuyerParty",
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
    purpose: Optional[Purpose] = field(
        default=None,
        metadata={
            "name": "Purpose",
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
    change_type: Optional[ChangeType] = field(
        default=None,
        metadata={
            "name": "ChangeType",
            "type": "Element",
            "required": True,
        }
    )
    order_type: Optional[OrderType] = field(
        default=None,
        metadata={
            "name": "OrderType",
            "type": "Element",
        }
    )
    original_order_header: Optional[OriginalOrderHeader] = field(
        default=None,
        metadata={
            "name": "OriginalOrderHeader",
            "type": "Element",
        }
    )
    order_header_changes: Optional[OrderHeaderChanges] = field(
        default=None,
        metadata={
            "name": "OrderHeaderChanges",
            "type": "Element",
        }
    )
    change_order_header_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChangeOrderHeaderNote",
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
class ListOfOrderResponseItemDetail:
    order_response_item_detail: List[OrderResponseItemDetail] = field(
        default_factory=list,
        metadata={
            "name": "OrderResponseItemDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ListOfOrderResponsePackageDetail:
    order_response_package_detail: List[OrderResponsePackageDetail] = field(
        default_factory=list,
        metadata={
            "name": "OrderResponsePackageDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class OrderResponseDetail:
    list_of_order_response_item_detail: Optional[ListOfOrderResponseItemDetail] = field(
        default=None,
        metadata={
            "name": "ListOfOrderResponseItemDetail",
            "type": "Element",
        }
    )
    list_of_order_response_package_detail: Optional[ListOfOrderResponsePackageDetail] = field(
        default=None,
        metadata={
            "name": "ListOfOrderResponsePackageDetail",
            "type": "Element",
        }
    )


@dataclass
class OrderResponseHeader:
    order_response_number: Optional[OrderResponseNumber] = field(
        default=None,
        metadata={
            "name": "OrderResponseNumber",
            "type": "Element",
            "required": True,
        }
    )
    order_response_issue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderResponseIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    order_response_doc_type_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderResponseDocTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    order_response_doc_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderResponseDocTypeCodedOther",
            "type": "Element",
        }
    )
    order_reference: Optional[OrderReference] = field(
        default=None,
        metadata={
            "name": "OrderReference",
            "type": "Element",
            "required": True,
        }
    )
    change_order_reference: Optional[ChangeOrderReference] = field(
        default=None,
        metadata={
            "name": "ChangeOrderReference",
            "type": "Element",
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
    buyer_party: Optional[BuyerParty] = field(
        default=None,
        metadata={
            "name": "BuyerParty",
            "type": "Element",
            "required": True,
        }
    )
    tracking_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrackingURL",
            "type": "Element",
        }
    )
    list_of_reference_coded: Optional[ListOfReferenceCoded] = field(
        default=None,
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
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
    order_status: Optional[OrderStatus] = field(
        default=None,
        metadata={
            "name": "OrderStatus",
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
    payment_status_event: Optional[PaymentStatusEvent] = field(
        default=None,
        metadata={
            "name": "PaymentStatusEvent",
            "type": "Element",
        }
    )
    original_order_header: Optional[OriginalOrderHeader] = field(
        default=None,
        metadata={
            "name": "OriginalOrderHeader",
            "type": "Element",
            "required": True,
        }
    )
    change_order_header: Optional[ChangeOrderHeader] = field(
        default=None,
        metadata={
            "name": "ChangeOrderHeader",
            "type": "Element",
            "required": True,
        }
    )
    order_header_changes: Optional[OrderHeaderChanges] = field(
        default=None,
        metadata={
            "name": "OrderHeaderChanges",
            "type": "Element",
        }
    )
    order_response_header_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderResponseHeaderNote",
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
class OrderResponse:
    order_response_header: Optional[OrderResponseHeader] = field(
        default=None,
        metadata={
            "name": "OrderResponseHeader",
            "type": "Element",
            "required": True,
        }
    )
    order_response_detail: Optional[OrderResponseDetail] = field(
        default=None,
        metadata={
            "name": "OrderResponseDetail",
            "type": "Element",
        }
    )
    order_response_summary: Optional[OrderResponseSummary] = field(
        default=None,
        metadata={
            "name": "OrderResponseSummary",
            "type": "Element",
        }
    )
