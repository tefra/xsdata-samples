from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.order_status_result import (
    ItemStatusEvent,
    OrderStatus,
    PaymentStatusEvent,
    ShipmentStatusEvent,
)
from xcbl.models.price_check_result import (
    ErrorInfo,
    PriceErrorInfo,
)
from xcbl.models.quote import TaxReference
from xcbl.models.request_for_quotation import PaymentInstructions
from xcbl.models.shipping_schedule import (
    OrderReferences,
    PackageDetail,
)
from xcbl.models.shipping_schedule_response import (
    ListOfMessageId,
    OrderNumber,
    OrderType,
    RequestedResponse,
    ResponseType,
)
from xcbl.models.sourcing_result import (
    BuyerParty,
    ItemDetail,
    ListOfAllowOrCharge,
    ListOfAttachment,
    ListOfNameValueSet,
    ListOfPrice,
    ListOfReferenceCoded,
    ListOfStructuredNote,
    MonetaryValue,
    OrderDates,
    OrderParty,
    RoundTripInformation,
    SellerParty,
    TermsOfDelivery,
    Transport,
)
from xcbl.models.sourcing_result_response import Purpose
from xcbl.models.time_series_response import Measurement
from xcbl.models.trading_partner_organization_information import Currency
from xcbl.models.trading_partner_response import Reference
from xcbl.models.trading_partner_user_information import Language


@dataclass(kw_only=True)
class ChangeType:
    change_type_coded: str = field(
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
        },
    )


@dataclass(kw_only=True)
class AvailabilityErrorInfo:
    error_info: ErrorInfo = field(
        metadata={
            "name": "ErrorInfo",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ChangeOrderNumber:
    buyer_change_order_number: str = field(
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
        },
    )
    list_of_message_id: Optional[ListOfMessageId] = field(
        default=None,
        metadata={
            "name": "ListOfMessageID",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ChangeOrderReference:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class GrossVolume:
    measurement: Measurement = field(
        metadata={
            "name": "Measurement",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ItemDetailChanges:
    item_detail: ItemDetail = field(
        metadata={
            "name": "ItemDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfErrorInfo:
    error_info: List[ErrorInfo] = field(
        default_factory=list,
        metadata={
            "name": "ErrorInfo",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ListOfTransport:
    transport: List[Transport] = field(
        default_factory=list,
        metadata={
            "name": "Transport",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class OrderAllowancesOrCharges:
    list_of_allow_or_charge: ListOfAllowOrCharge = field(
        metadata={
            "name": "ListOfAllowOrCharge",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderCurrency:
    currency: Currency = field(
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderHeaderAttachments:
    list_of_attachment: ListOfAttachment = field(
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderHeaderPrice:
    list_of_price: ListOfPrice = field(
        metadata={
            "name": "ListOfPrice",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderLanguage:
    language: Language = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderPaymentInstructions:
    payment_instructions: PaymentInstructions = field(
        metadata={
            "name": "PaymentInstructions",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderReference:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderResponseNumber:
    buyer_order_response_number: str = field(
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
        },
    )
    list_of_message_id: Optional[ListOfMessageId] = field(
        default=None,
        metadata={
            "name": "ListOfMessageID",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class OrderTaxReference:
    tax_reference: TaxReference = field(
        metadata={
            "name": "TaxReference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderTermsOfDelivery:
    terms_of_delivery: TermsOfDelivery = field(
        metadata={
            "name": "TermsOfDelivery",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OriginalItemDetail:
    item_detail: ItemDetail = field(
        metadata={
            "name": "ItemDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OriginalPackageDetail:
    package_detail: PackageDetail = field(
        metadata={
            "name": "PackageDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PackageDetailChanges:
    package_detail: PackageDetail = field(
        metadata={
            "name": "PackageDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TaxAccountingCurrency:
    currency: Currency = field(
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TotalAmount:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TotalGrossWeight:
    measurement: Measurement = field(
        metadata={
            "name": "Measurement",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TotalNetNetWeight:
    measurement: Measurement = field(
        metadata={
            "name": "Measurement",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TotalNetWeight:
    measurement: Measurement = field(
        metadata={
            "name": "Measurement",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TotalTareWeight:
    measurement: Measurement = field(
        metadata={
            "name": "Measurement",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TotalTax:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ChangeOrderItemDetail:
    item_detail_change_coded: str = field(
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
        },
    )
    list_of_reference_coded: Optional[ListOfReferenceCoded] = field(
        default=None,
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
        },
    )
    original_item_detail: Optional[OriginalItemDetail] = field(
        default=None,
        metadata={
            "name": "OriginalItemDetail",
            "type": "Element",
        },
    )
    item_detail_changes: Optional[ItemDetailChanges] = field(
        default=None,
        metadata={
            "name": "ItemDetailChanges",
            "type": "Element",
        },
    )
    line_item_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineItemNote",
            "type": "Element",
        },
    )
    list_of_structured_note: Optional[ListOfStructuredNote] = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ChangeOrderPackageDetail:
    package_detail_change_coded: str = field(
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
        },
    )
    original_package_detail: Optional[OriginalPackageDetail] = field(
        default=None,
        metadata={
            "name": "OriginalPackageDetail",
            "type": "Element",
        },
    )
    package_detail_changes: Optional[PackageDetailChanges] = field(
        default=None,
        metadata={
            "name": "PackageDetailChanges",
            "type": "Element",
        },
    )
    package_detail_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "PackageDetailNote",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class OrderHeader:
    order_number: OrderNumber = field(
        metadata={
            "name": "OrderNumber",
            "type": "Element",
            "required": True,
        }
    )
    order_issue_date: str = field(
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
        },
    )
    release_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReleaseNumber",
            "type": "Element",
        },
    )
    purpose: Purpose = field(
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
        },
    )
    order_type: Optional[OrderType] = field(
        default=None,
        metadata={
            "name": "OrderType",
            "type": "Element",
        },
    )
    order_currency: OrderCurrency = field(
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
        },
    )
    order_language: OrderLanguage = field(
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
        },
    )
    order_invoice_medium_type_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderInvoiceMediumTypeCoded",
            "type": "Element",
        },
    )
    order_invoice_medium_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderInvoiceMediumTypeCodedOther",
            "type": "Element",
        },
    )
    order_dates: Optional[OrderDates] = field(
        default=None,
        metadata={
            "name": "OrderDates",
            "type": "Element",
        },
    )
    partial_shipment_allowed: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartialShipmentAllowed",
            "type": "Element",
        },
    )
    order_party: OrderParty = field(
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
        },
    )
    list_of_transport: Optional[ListOfTransport] = field(
        default=None,
        metadata={
            "name": "ListOfTransport",
            "type": "Element",
        },
    )
    order_terms_of_delivery: List[OrderTermsOfDelivery] = field(
        default_factory=list,
        metadata={
            "name": "OrderTermsOfDelivery",
            "type": "Element",
        },
    )
    order_header_price: Optional[OrderHeaderPrice] = field(
        default=None,
        metadata={
            "name": "OrderHeaderPrice",
            "type": "Element",
        },
    )
    order_payment_instructions: Optional[OrderPaymentInstructions] = field(
        default=None,
        metadata={
            "name": "OrderPaymentInstructions",
            "type": "Element",
        },
    )
    order_allowances_or_charges: Optional[OrderAllowancesOrCharges] = field(
        default=None,
        metadata={
            "name": "OrderAllowancesOrCharges",
            "type": "Element",
        },
    )
    round_trip_information: Optional[RoundTripInformation] = field(
        default=None,
        metadata={
            "name": "RoundTripInformation",
            "type": "Element",
        },
    )
    order_header_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderHeaderNote",
            "type": "Element",
        },
    )
    list_of_structured_note: Optional[ListOfStructuredNote] = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        },
    )
    list_of_name_value_set: Optional[ListOfNameValueSet] = field(
        default=None,
        metadata={
            "name": "ListOfNameValueSet",
            "type": "Element",
        },
    )
    order_header_attachments: Optional[OrderHeaderAttachments] = field(
        default=None,
        metadata={
            "name": "OrderHeaderAttachments",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class TransportPackagingTotals:
    total_packages: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalPackages",
            "type": "Element",
        },
    )
    total_package_depth: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalPackageDepth",
            "type": "Element",
        },
    )
    total_transport: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalTransport",
            "type": "Element",
        },
    )
    total_gross_weight: Optional[TotalGrossWeight] = field(
        default=None,
        metadata={
            "name": "TotalGrossWeight",
            "type": "Element",
        },
    )
    total_net_weight: Optional[TotalNetWeight] = field(
        default=None,
        metadata={
            "name": "TotalNetWeight",
            "type": "Element",
        },
    )
    total_net_net_weight: Optional[TotalNetNetWeight] = field(
        default=None,
        metadata={
            "name": "TotalNetNetWeight",
            "type": "Element",
        },
    )
    total_tare_weight: Optional[TotalTareWeight] = field(
        default=None,
        metadata={
            "name": "TotalTareWeight",
            "type": "Element",
        },
    )
    gross_volume: Optional[GrossVolume] = field(
        default=None,
        metadata={
            "name": "GrossVolume",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class OrderHeaderChanges:
    order_header: OrderHeader = field(
        metadata={
            "name": "OrderHeader",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderResponseItemDetail:
    item_detail_response_coded: str = field(
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
        },
    )
    item_status_event: Optional[ItemStatusEvent] = field(
        default=None,
        metadata={
            "name": "ItemStatusEvent",
            "type": "Element",
        },
    )
    shipment_status_event: Optional[ShipmentStatusEvent] = field(
        default=None,
        metadata={
            "name": "ShipmentStatusEvent",
            "type": "Element",
        },
    )
    payment_status_event: Optional[PaymentStatusEvent] = field(
        default=None,
        metadata={
            "name": "PaymentStatusEvent",
            "type": "Element",
        },
    )
    price_error_info: Optional[PriceErrorInfo] = field(
        default=None,
        metadata={
            "name": "PriceErrorInfo",
            "type": "Element",
        },
    )
    availability_error_info: Optional[AvailabilityErrorInfo] = field(
        default=None,
        metadata={
            "name": "AvailabilityErrorInfo",
            "type": "Element",
        },
    )
    list_of_error_info: Optional[ListOfErrorInfo] = field(
        default=None,
        metadata={
            "name": "ListOfErrorInfo",
            "type": "Element",
        },
    )
    tracking_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrackingURL",
            "type": "Element",
        },
    )
    list_of_reference_coded: Optional[ListOfReferenceCoded] = field(
        default=None,
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
        },
    )
    original_item_detail: Optional[OriginalItemDetail] = field(
        default=None,
        metadata={
            "name": "OriginalItemDetail",
            "type": "Element",
        },
    )
    change_order_item_detail: Optional[ChangeOrderItemDetail] = field(
        default=None,
        metadata={
            "name": "ChangeOrderItemDetail",
            "type": "Element",
        },
    )
    item_detail_changes: Optional[ItemDetailChanges] = field(
        default=None,
        metadata={
            "name": "ItemDetailChanges",
            "type": "Element",
        },
    )
    line_item_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineItemNote",
            "type": "Element",
        },
    )
    list_of_structured_note: Optional[ListOfStructuredNote] = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class OrderResponsePackageDetail:
    package_detail_response_coded: str = field(
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
        },
    )
    original_package_detail: Optional[OriginalPackageDetail] = field(
        default=None,
        metadata={
            "name": "OriginalPackageDetail",
            "type": "Element",
        },
    )
    change_order_package_detail: Optional[ChangeOrderPackageDetail] = field(
        default=None,
        metadata={
            "name": "ChangeOrderPackageDetail",
            "type": "Element",
        },
    )
    package_detail_changes: Optional[PackageDetailChanges] = field(
        default=None,
        metadata={
            "name": "PackageDetailChanges",
            "type": "Element",
        },
    )
    package_detail_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "PackageDetailNote",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class OrderSummary:
    number_of_lines: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumberOfLines",
            "type": "Element",
        },
    )
    total_tax: Optional[TotalTax] = field(
        default=None,
        metadata={
            "name": "TotalTax",
            "type": "Element",
        },
    )
    total_amount: Optional[TotalAmount] = field(
        default=None,
        metadata={
            "name": "TotalAmount",
            "type": "Element",
        },
    )
    transport_packaging_totals: Optional[TransportPackagingTotals] = field(
        default=None,
        metadata={
            "name": "TransportPackagingTotals",
            "type": "Element",
        },
    )
    summary_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "SummaryNote",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class OriginalOrderHeader:
    order_header: OrderHeader = field(
        metadata={
            "name": "OrderHeader",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ChangeOrderHeader:
    change_order_number: ChangeOrderNumber = field(
        metadata={
            "name": "ChangeOrderNumber",
            "type": "Element",
            "required": True,
        }
    )
    change_order_sequence: str = field(
        metadata={
            "name": "ChangeOrderSequence",
            "type": "Element",
            "required": True,
        }
    )
    change_order_issue_date: str = field(
        metadata={
            "name": "ChangeOrderIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    order_reference: OrderReference = field(
        metadata={
            "name": "OrderReference",
            "type": "Element",
            "required": True,
        }
    )
    seller_party: SellerParty = field(
        metadata={
            "name": "SellerParty",
            "type": "Element",
            "required": True,
        }
    )
    buyer_party: BuyerParty = field(
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
        },
    )
    purpose: Purpose = field(
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
        },
    )
    change_type: ChangeType = field(
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
        },
    )
    original_order_header: Optional[OriginalOrderHeader] = field(
        default=None,
        metadata={
            "name": "OriginalOrderHeader",
            "type": "Element",
        },
    )
    order_header_changes: Optional[OrderHeaderChanges] = field(
        default=None,
        metadata={
            "name": "OrderHeaderChanges",
            "type": "Element",
        },
    )
    change_order_header_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChangeOrderHeaderNote",
            "type": "Element",
        },
    )
    list_of_structured_note: Optional[ListOfStructuredNote] = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfOrderResponseItemDetail:
    order_response_item_detail: List[OrderResponseItemDetail] = field(
        default_factory=list,
        metadata={
            "name": "OrderResponseItemDetail",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ListOfOrderResponsePackageDetail:
    order_response_package_detail: List[OrderResponsePackageDetail] = field(
        default_factory=list,
        metadata={
            "name": "OrderResponsePackageDetail",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class OriginalOrderSummary:
    order_summary: OrderSummary = field(
        metadata={
            "name": "OrderSummary",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RevisedOrderSummary:
    order_summary: OrderSummary = field(
        metadata={
            "name": "OrderSummary",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderResponseDetail:
    list_of_order_response_item_detail: Optional[
        ListOfOrderResponseItemDetail
    ] = field(
        default=None,
        metadata={
            "name": "ListOfOrderResponseItemDetail",
            "type": "Element",
        },
    )
    list_of_order_response_package_detail: Optional[
        ListOfOrderResponsePackageDetail
    ] = field(
        default=None,
        metadata={
            "name": "ListOfOrderResponsePackageDetail",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class OrderResponseHeader:
    order_response_number: OrderResponseNumber = field(
        metadata={
            "name": "OrderResponseNumber",
            "type": "Element",
            "required": True,
        }
    )
    order_response_issue_date: str = field(
        metadata={
            "name": "OrderResponseIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    order_response_doc_type_coded: str = field(
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
        },
    )
    order_reference: OrderReference = field(
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
        },
    )
    seller_party: SellerParty = field(
        metadata={
            "name": "SellerParty",
            "type": "Element",
            "required": True,
        }
    )
    buyer_party: BuyerParty = field(
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
        },
    )
    list_of_reference_coded: Optional[ListOfReferenceCoded] = field(
        default=None,
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
        },
    )
    purpose: Purpose = field(
        metadata={
            "name": "Purpose",
            "type": "Element",
            "required": True,
        }
    )
    response_type: ResponseType = field(
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
        },
    )
    shipment_status_event: Optional[ShipmentStatusEvent] = field(
        default=None,
        metadata={
            "name": "ShipmentStatusEvent",
            "type": "Element",
        },
    )
    payment_status_event: Optional[PaymentStatusEvent] = field(
        default=None,
        metadata={
            "name": "PaymentStatusEvent",
            "type": "Element",
        },
    )
    original_order_header: Optional[OriginalOrderHeader] = field(
        default=None,
        metadata={
            "name": "OriginalOrderHeader",
            "type": "Element",
        },
    )
    change_order_header: Optional[ChangeOrderHeader] = field(
        default=None,
        metadata={
            "name": "ChangeOrderHeader",
            "type": "Element",
        },
    )
    order_header_changes: Optional[OrderHeaderChanges] = field(
        default=None,
        metadata={
            "name": "OrderHeaderChanges",
            "type": "Element",
        },
    )
    order_response_header_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderResponseHeaderNote",
            "type": "Element",
        },
    )
    list_of_structured_note: Optional[ListOfStructuredNote] = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class OrderResponseSummary:
    error_info: Optional[ErrorInfo] = field(
        default=None,
        metadata={
            "name": "ErrorInfo",
            "type": "Element",
        },
    )
    original_order_summary: Optional[OriginalOrderSummary] = field(
        default=None,
        metadata={
            "name": "OriginalOrderSummary",
            "type": "Element",
        },
    )
    revised_order_summary: Optional[RevisedOrderSummary] = field(
        default=None,
        metadata={
            "name": "RevisedOrderSummary",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class OrderResponse:
    order_response_header: OrderResponseHeader = field(
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
        },
    )
    order_response_summary: Optional[OrderResponseSummary] = field(
        default=None,
        metadata={
            "name": "OrderResponseSummary",
            "type": "Element",
        },
    )
