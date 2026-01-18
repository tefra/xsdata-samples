from dataclasses import dataclass, field

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
from xcbl.models.remittance_advice import SummaryNote
from xcbl.models.request_for_quotation import PaymentInstructions
from xcbl.models.shipping_schedule import (
    OrderReferences,
    PackageDetail,
)
from xcbl.models.shipping_schedule_response import (
    ListOfMessageId,
    OrderIssueDate,
    OrderNumber,
    OrderType,
    ReleaseNumber,
    RequestedResponse,
    ResponseType,
)
from xcbl.models.sourcing_result import (
    BuyerParty,
    ItemDetail,
    LineItemNote,
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
class BuyerChangeOrderNumber:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class BuyerOrderResponseNumber:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ChangeOrderHeaderNote:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ChangeOrderIssueDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ChangeOrderSequence:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ChangeTypeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ChangeTypeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ItemDetailChangeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ItemDetailChangeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ItemDetailResponseCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ItemDetailResponseCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class NumberOfLines:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class OrderHeaderNote:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class OrderInvoiceMediumTypeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class OrderInvoiceMediumTypeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class OrderResponseDocTypeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class OrderResponseDocTypeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class OrderResponseHeaderNote:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class OrderResponseIssueDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PackageDetailChangeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PackageDetailChangeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PackageDetailNote:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PackageDetailResponseCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PackageDetailResponseCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PartLocation:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PartialShipmentAllowed:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SellerChangeOrderNumber:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SellerOrderResponseNumber:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TotalPackageDepth:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TotalPackages:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TotalTransport:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TrackingUrl:
    class Meta:
        name = "TrackingURL"

    value: str = field(
        default="",
        metadata={
            "required": True,
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
    buyer_change_order_number: BuyerChangeOrderNumber = field(
        metadata={
            "name": "BuyerChangeOrderNumber",
            "type": "Element",
            "required": True,
        }
    )
    seller_change_order_number: SellerChangeOrderNumber | None = field(
        default=None,
        metadata={
            "name": "SellerChangeOrderNumber",
            "type": "Element",
        },
    )
    list_of_message_id: ListOfMessageId | None = field(
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
class ChangeType:
    change_type_coded: ChangeTypeCoded = field(
        metadata={
            "name": "ChangeTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    change_type_coded_other: ChangeTypeCodedOther | None = field(
        default=None,
        metadata={
            "name": "ChangeTypeCodedOther",
            "type": "Element",
        },
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
    error_info: list[ErrorInfo] = field(
        default_factory=list,
        metadata={
            "name": "ErrorInfo",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ListOfTransport:
    transport: list[Transport] = field(
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
    buyer_order_response_number: BuyerOrderResponseNumber = field(
        metadata={
            "name": "BuyerOrderResponseNumber",
            "type": "Element",
            "required": True,
        }
    )
    seller_order_response_number: SellerOrderResponseNumber | None = field(
        default=None,
        metadata={
            "name": "SellerOrderResponseNumber",
            "type": "Element",
        },
    )
    list_of_message_id: ListOfMessageId | None = field(
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
    item_detail_change_coded: ItemDetailChangeCoded = field(
        metadata={
            "name": "ItemDetailChangeCoded",
            "type": "Element",
            "required": True,
        }
    )
    item_detail_change_coded_other: ItemDetailChangeCodedOther | None = field(
        default=None,
        metadata={
            "name": "ItemDetailChangeCodedOther",
            "type": "Element",
        },
    )
    list_of_reference_coded: ListOfReferenceCoded | None = field(
        default=None,
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
        },
    )
    original_item_detail: OriginalItemDetail | None = field(
        default=None,
        metadata={
            "name": "OriginalItemDetail",
            "type": "Element",
        },
    )
    item_detail_changes: ItemDetailChanges | None = field(
        default=None,
        metadata={
            "name": "ItemDetailChanges",
            "type": "Element",
        },
    )
    line_item_note: LineItemNote | None = field(
        default=None,
        metadata={
            "name": "LineItemNote",
            "type": "Element",
        },
    )
    list_of_structured_note: ListOfStructuredNote | None = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ChangeOrderPackageDetail:
    package_detail_change_coded: PackageDetailChangeCoded = field(
        metadata={
            "name": "PackageDetailChangeCoded",
            "type": "Element",
            "required": True,
        }
    )
    package_detail_change_coded_other: PackageDetailChangeCodedOther | None = (
        field(
            default=None,
            metadata={
                "name": "PackageDetailChangeCodedOther",
                "type": "Element",
            },
        )
    )
    original_package_detail: OriginalPackageDetail | None = field(
        default=None,
        metadata={
            "name": "OriginalPackageDetail",
            "type": "Element",
        },
    )
    package_detail_changes: PackageDetailChanges | None = field(
        default=None,
        metadata={
            "name": "PackageDetailChanges",
            "type": "Element",
        },
    )
    package_detail_note: PackageDetailNote | None = field(
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
    order_issue_date: OrderIssueDate = field(
        metadata={
            "name": "OrderIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    order_references: OrderReferences | None = field(
        default=None,
        metadata={
            "name": "OrderReferences",
            "type": "Element",
        },
    )
    release_number: ReleaseNumber | None = field(
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
    requested_response: RequestedResponse | None = field(
        default=None,
        metadata={
            "name": "RequestedResponse",
            "type": "Element",
        },
    )
    order_type: OrderType | None = field(
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
    tax_accounting_currency: TaxAccountingCurrency | None = field(
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
    order_tax_reference: OrderTaxReference | None = field(
        default=None,
        metadata={
            "name": "OrderTaxReference",
            "type": "Element",
        },
    )
    order_invoice_medium_type_coded: OrderInvoiceMediumTypeCoded | None = (
        field(
            default=None,
            metadata={
                "name": "OrderInvoiceMediumTypeCoded",
                "type": "Element",
            },
        )
    )
    order_invoice_medium_type_coded_other: (
        OrderInvoiceMediumTypeCodedOther | None
    ) = field(
        default=None,
        metadata={
            "name": "OrderInvoiceMediumTypeCodedOther",
            "type": "Element",
        },
    )
    order_dates: OrderDates | None = field(
        default=None,
        metadata={
            "name": "OrderDates",
            "type": "Element",
        },
    )
    partial_shipment_allowed: PartialShipmentAllowed | None = field(
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
    part_location: PartLocation | None = field(
        default=None,
        metadata={
            "name": "PartLocation",
            "type": "Element",
        },
    )
    list_of_transport: ListOfTransport | None = field(
        default=None,
        metadata={
            "name": "ListOfTransport",
            "type": "Element",
        },
    )
    order_terms_of_delivery: list[OrderTermsOfDelivery] = field(
        default_factory=list,
        metadata={
            "name": "OrderTermsOfDelivery",
            "type": "Element",
        },
    )
    order_header_price: OrderHeaderPrice | None = field(
        default=None,
        metadata={
            "name": "OrderHeaderPrice",
            "type": "Element",
        },
    )
    order_payment_instructions: OrderPaymentInstructions | None = field(
        default=None,
        metadata={
            "name": "OrderPaymentInstructions",
            "type": "Element",
        },
    )
    order_allowances_or_charges: OrderAllowancesOrCharges | None = field(
        default=None,
        metadata={
            "name": "OrderAllowancesOrCharges",
            "type": "Element",
        },
    )
    round_trip_information: RoundTripInformation | None = field(
        default=None,
        metadata={
            "name": "RoundTripInformation",
            "type": "Element",
        },
    )
    order_header_note: OrderHeaderNote | None = field(
        default=None,
        metadata={
            "name": "OrderHeaderNote",
            "type": "Element",
        },
    )
    list_of_structured_note: ListOfStructuredNote | None = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        },
    )
    list_of_name_value_set: ListOfNameValueSet | None = field(
        default=None,
        metadata={
            "name": "ListOfNameValueSet",
            "type": "Element",
        },
    )
    order_header_attachments: OrderHeaderAttachments | None = field(
        default=None,
        metadata={
            "name": "OrderHeaderAttachments",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class TransportPackagingTotals:
    total_packages: TotalPackages | None = field(
        default=None,
        metadata={
            "name": "TotalPackages",
            "type": "Element",
        },
    )
    total_package_depth: TotalPackageDepth | None = field(
        default=None,
        metadata={
            "name": "TotalPackageDepth",
            "type": "Element",
        },
    )
    total_transport: TotalTransport | None = field(
        default=None,
        metadata={
            "name": "TotalTransport",
            "type": "Element",
        },
    )
    total_gross_weight: TotalGrossWeight | None = field(
        default=None,
        metadata={
            "name": "TotalGrossWeight",
            "type": "Element",
        },
    )
    total_net_weight: TotalNetWeight | None = field(
        default=None,
        metadata={
            "name": "TotalNetWeight",
            "type": "Element",
        },
    )
    total_net_net_weight: TotalNetNetWeight | None = field(
        default=None,
        metadata={
            "name": "TotalNetNetWeight",
            "type": "Element",
        },
    )
    total_tare_weight: TotalTareWeight | None = field(
        default=None,
        metadata={
            "name": "TotalTareWeight",
            "type": "Element",
        },
    )
    gross_volume: GrossVolume | None = field(
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
    item_detail_response_coded: ItemDetailResponseCoded = field(
        metadata={
            "name": "ItemDetailResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    item_detail_response_coded_other: ItemDetailResponseCodedOther | None = (
        field(
            default=None,
            metadata={
                "name": "ItemDetailResponseCodedOther",
                "type": "Element",
            },
        )
    )
    item_status_event: ItemStatusEvent | None = field(
        default=None,
        metadata={
            "name": "ItemStatusEvent",
            "type": "Element",
        },
    )
    shipment_status_event: ShipmentStatusEvent | None = field(
        default=None,
        metadata={
            "name": "ShipmentStatusEvent",
            "type": "Element",
        },
    )
    payment_status_event: PaymentStatusEvent | None = field(
        default=None,
        metadata={
            "name": "PaymentStatusEvent",
            "type": "Element",
        },
    )
    price_error_info: PriceErrorInfo | None = field(
        default=None,
        metadata={
            "name": "PriceErrorInfo",
            "type": "Element",
        },
    )
    availability_error_info: AvailabilityErrorInfo | None = field(
        default=None,
        metadata={
            "name": "AvailabilityErrorInfo",
            "type": "Element",
        },
    )
    list_of_error_info: ListOfErrorInfo | None = field(
        default=None,
        metadata={
            "name": "ListOfErrorInfo",
            "type": "Element",
        },
    )
    tracking_url: TrackingUrl | None = field(
        default=None,
        metadata={
            "name": "TrackingURL",
            "type": "Element",
        },
    )
    list_of_reference_coded: ListOfReferenceCoded | None = field(
        default=None,
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
        },
    )
    original_item_detail: OriginalItemDetail | None = field(
        default=None,
        metadata={
            "name": "OriginalItemDetail",
            "type": "Element",
        },
    )
    change_order_item_detail: ChangeOrderItemDetail | None = field(
        default=None,
        metadata={
            "name": "ChangeOrderItemDetail",
            "type": "Element",
        },
    )
    item_detail_changes: ItemDetailChanges | None = field(
        default=None,
        metadata={
            "name": "ItemDetailChanges",
            "type": "Element",
        },
    )
    line_item_note: LineItemNote | None = field(
        default=None,
        metadata={
            "name": "LineItemNote",
            "type": "Element",
        },
    )
    list_of_structured_note: ListOfStructuredNote | None = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class OrderResponsePackageDetail:
    package_detail_response_coded: PackageDetailResponseCoded = field(
        metadata={
            "name": "PackageDetailResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    package_detail_response_coded_other: (
        PackageDetailResponseCodedOther | None
    ) = field(
        default=None,
        metadata={
            "name": "PackageDetailResponseCodedOther",
            "type": "Element",
        },
    )
    original_package_detail: OriginalPackageDetail | None = field(
        default=None,
        metadata={
            "name": "OriginalPackageDetail",
            "type": "Element",
        },
    )
    change_order_package_detail: ChangeOrderPackageDetail | None = field(
        default=None,
        metadata={
            "name": "ChangeOrderPackageDetail",
            "type": "Element",
        },
    )
    package_detail_changes: PackageDetailChanges | None = field(
        default=None,
        metadata={
            "name": "PackageDetailChanges",
            "type": "Element",
        },
    )
    package_detail_note: PackageDetailNote | None = field(
        default=None,
        metadata={
            "name": "PackageDetailNote",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class OrderSummary:
    number_of_lines: NumberOfLines | None = field(
        default=None,
        metadata={
            "name": "NumberOfLines",
            "type": "Element",
        },
    )
    total_tax: TotalTax | None = field(
        default=None,
        metadata={
            "name": "TotalTax",
            "type": "Element",
        },
    )
    total_amount: TotalAmount | None = field(
        default=None,
        metadata={
            "name": "TotalAmount",
            "type": "Element",
        },
    )
    transport_packaging_totals: TransportPackagingTotals | None = field(
        default=None,
        metadata={
            "name": "TransportPackagingTotals",
            "type": "Element",
        },
    )
    summary_note: SummaryNote | None = field(
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
    change_order_sequence: ChangeOrderSequence = field(
        metadata={
            "name": "ChangeOrderSequence",
            "type": "Element",
            "required": True,
        }
    )
    change_order_issue_date: ChangeOrderIssueDate = field(
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
    list_of_reference_coded: ListOfReferenceCoded | None = field(
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
    requested_response: RequestedResponse | None = field(
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
    order_type: OrderType | None = field(
        default=None,
        metadata={
            "name": "OrderType",
            "type": "Element",
        },
    )
    original_order_header: OriginalOrderHeader | None = field(
        default=None,
        metadata={
            "name": "OriginalOrderHeader",
            "type": "Element",
        },
    )
    order_header_changes: OrderHeaderChanges | None = field(
        default=None,
        metadata={
            "name": "OrderHeaderChanges",
            "type": "Element",
        },
    )
    change_order_header_note: ChangeOrderHeaderNote | None = field(
        default=None,
        metadata={
            "name": "ChangeOrderHeaderNote",
            "type": "Element",
        },
    )
    list_of_structured_note: ListOfStructuredNote | None = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfOrderResponseItemDetail:
    order_response_item_detail: list[OrderResponseItemDetail] = field(
        default_factory=list,
        metadata={
            "name": "OrderResponseItemDetail",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ListOfOrderResponsePackageDetail:
    order_response_package_detail: list[OrderResponsePackageDetail] = field(
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
    list_of_order_response_item_detail: (
        ListOfOrderResponseItemDetail | None
    ) = field(
        default=None,
        metadata={
            "name": "ListOfOrderResponseItemDetail",
            "type": "Element",
        },
    )
    list_of_order_response_package_detail: (
        ListOfOrderResponsePackageDetail | None
    ) = field(
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
    order_response_issue_date: OrderResponseIssueDate = field(
        metadata={
            "name": "OrderResponseIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    order_response_doc_type_coded: OrderResponseDocTypeCoded = field(
        metadata={
            "name": "OrderResponseDocTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    order_response_doc_type_coded_other: (
        OrderResponseDocTypeCodedOther | None
    ) = field(
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
    change_order_reference: ChangeOrderReference | None = field(
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
    tracking_url: TrackingUrl | None = field(
        default=None,
        metadata={
            "name": "TrackingURL",
            "type": "Element",
        },
    )
    list_of_reference_coded: ListOfReferenceCoded | None = field(
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
    order_status: OrderStatus | None = field(
        default=None,
        metadata={
            "name": "OrderStatus",
            "type": "Element",
        },
    )
    shipment_status_event: ShipmentStatusEvent | None = field(
        default=None,
        metadata={
            "name": "ShipmentStatusEvent",
            "type": "Element",
        },
    )
    payment_status_event: PaymentStatusEvent | None = field(
        default=None,
        metadata={
            "name": "PaymentStatusEvent",
            "type": "Element",
        },
    )
    original_order_header: OriginalOrderHeader | None = field(
        default=None,
        metadata={
            "name": "OriginalOrderHeader",
            "type": "Element",
        },
    )
    change_order_header: ChangeOrderHeader | None = field(
        default=None,
        metadata={
            "name": "ChangeOrderHeader",
            "type": "Element",
        },
    )
    order_header_changes: OrderHeaderChanges | None = field(
        default=None,
        metadata={
            "name": "OrderHeaderChanges",
            "type": "Element",
        },
    )
    order_response_header_note: OrderResponseHeaderNote | None = field(
        default=None,
        metadata={
            "name": "OrderResponseHeaderNote",
            "type": "Element",
        },
    )
    list_of_structured_note: ListOfStructuredNote | None = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class OrderResponseSummary:
    error_info: ErrorInfo | None = field(
        default=None,
        metadata={
            "name": "ErrorInfo",
            "type": "Element",
        },
    )
    original_order_summary: OriginalOrderSummary | None = field(
        default=None,
        metadata={
            "name": "OriginalOrderSummary",
            "type": "Element",
        },
    )
    revised_order_summary: RevisedOrderSummary | None = field(
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
    order_response_detail: OrderResponseDetail | None = field(
        default=None,
        metadata={
            "name": "OrderResponseDetail",
            "type": "Element",
        },
    )
    order_response_summary: OrderResponseSummary | None = field(
        default=None,
        metadata={
            "name": "OrderResponseSummary",
            "type": "Element",
        },
    )
