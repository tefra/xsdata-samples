from __future__ import annotations

from dataclasses import dataclass, field

from xcbl.models.order_response import (
    ListOfTransport,
    OrderAllowancesOrCharges,
    OrderHeaderAttachments,
    OrderHeaderNote,
    OrderHeaderPrice,
    OrderInvoiceMediumTypeCoded,
    OrderInvoiceMediumTypeCodedOther,
    OrderPaymentInstructions,
    OrderSummary,
    OrderTermsOfDelivery,
    PartialShipmentAllowed,
    TaxAccountingCurrency,
)
from xcbl.models.quote import TaxReference
from xcbl.models.shipping_schedule import (
    ListOfPackageDetail,
    OrderReferences,
)
from xcbl.models.shipping_schedule_response import (
    ListOfMessageId,
    RequestedResponse,
)
from xcbl.models.sourcing_result import (
    BillToParty,
    BuyerParty,
    BuyerTaxInformation,
    ItemDetail,
    ListOfStructuredNote,
    OrderDates,
    RemitToParty,
    RoundTripInformation,
    SellerParty,
    SellerTaxInformation,
    ShipFromParty,
    ShipToParty,
)
from xcbl.models.sourcing_result_response import Purpose
from xcbl.models.time_series_response import ListOfPartyCoded
from xcbl.models.trading_partner_organization_information import Currency
from xcbl.models.trading_partner_user_information import Language


@dataclass(kw_only=True)
class BuyerOrderRequestNumber:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class OrderRequestIssueDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SellerOrderRequestNumber:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ListOfItemDetail:
    item_detail: list[ItemDetail] = field(
        default_factory=list,
        metadata={
            "name": "ItemDetail",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class OrderRequestCurrency:
    currency: Currency = field(
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderRequestDates:
    order_dates: OrderDates = field(
        metadata={
            "name": "OrderDates",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderRequestLanguage:
    language: Language = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderRequestNumber:
    buyer_order_request_number: BuyerOrderRequestNumber = field(
        metadata={
            "name": "BuyerOrderRequestNumber",
            "type": "Element",
            "required": True,
        }
    )
    seller_order_request_number: SellerOrderRequestNumber | None = field(
        default=None,
        metadata={
            "name": "SellerOrderRequestNumber",
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
class OrderRequestParty:
    buyer_party: BuyerParty | None = field(
        default=None,
        metadata={
            "name": "BuyerParty",
            "type": "Element",
        },
    )
    buyer_tax_information: BuyerTaxInformation | None = field(
        default=None,
        metadata={
            "name": "BuyerTaxInformation",
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
    seller_tax_information: SellerTaxInformation | None = field(
        default=None,
        metadata={
            "name": "SellerTaxInformation",
            "type": "Element",
        },
    )
    ship_to_party: ShipToParty | None = field(
        default=None,
        metadata={
            "name": "ShipToParty",
            "type": "Element",
        },
    )
    bill_to_party: BillToParty | None = field(
        default=None,
        metadata={
            "name": "BillToParty",
            "type": "Element",
        },
    )
    remit_to_party: RemitToParty | None = field(
        default=None,
        metadata={
            "name": "RemitToParty",
            "type": "Element",
        },
    )
    ship_from_party: ShipFromParty | None = field(
        default=None,
        metadata={
            "name": "ShipFromParty",
            "type": "Element",
        },
    )
    list_of_party_coded: ListOfPartyCoded | None = field(
        default=None,
        metadata={
            "name": "ListOfPartyCoded",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class OrderRequestReferences:
    order_references: OrderReferences = field(
        metadata={
            "name": "OrderReferences",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderRequestSummary:
    order_summary: OrderSummary = field(
        metadata={
            "name": "OrderSummary",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderRequestTaxReference:
    tax_reference: TaxReference = field(
        metadata={
            "name": "TaxReference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderDetail:
    list_of_item_detail: ListOfItemDetail = field(
        metadata={
            "name": "ListOfItemDetail",
            "type": "Element",
            "required": True,
        }
    )
    list_of_package_detail: ListOfPackageDetail | None = field(
        default=None,
        metadata={
            "name": "ListOfPackageDetail",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class OrderRequestHeader:
    order_request_number: OrderRequestNumber | None = field(
        default=None,
        metadata={
            "name": "OrderRequestNumber",
            "type": "Element",
        },
    )
    order_request_issue_date: OrderRequestIssueDate = field(
        metadata={
            "name": "OrderRequestIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    order_request_references: OrderRequestReferences | None = field(
        default=None,
        metadata={
            "name": "OrderRequestReferences",
            "type": "Element",
        },
    )
    purpose: Purpose | None = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Element",
        },
    )
    requested_response: RequestedResponse | None = field(
        default=None,
        metadata={
            "name": "RequestedResponse",
            "type": "Element",
        },
    )
    order_request_currency: OrderRequestCurrency = field(
        metadata={
            "name": "OrderRequestCurrency",
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
    order_request_language: OrderRequestLanguage = field(
        metadata={
            "name": "OrderRequestLanguage",
            "type": "Element",
            "required": True,
        }
    )
    order_request_tax_reference: OrderRequestTaxReference | None = field(
        default=None,
        metadata={
            "name": "OrderRequestTaxReference",
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
    order_request_dates: OrderRequestDates | None = field(
        default=None,
        metadata={
            "name": "OrderRequestDates",
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
    order_request_party: OrderRequestParty = field(
        metadata={
            "name": "OrderRequestParty",
            "type": "Element",
            "required": True,
        }
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
    order_header_attachments: OrderHeaderAttachments | None = field(
        default=None,
        metadata={
            "name": "OrderHeaderAttachments",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class OrderRequestDetail:
    order_detail: OrderDetail = field(
        metadata={
            "name": "OrderDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderRequest:
    order_request_header: OrderRequestHeader = field(
        metadata={
            "name": "OrderRequestHeader",
            "type": "Element",
            "required": True,
        }
    )
    order_request_detail: OrderRequestDetail | None = field(
        default=None,
        metadata={
            "name": "OrderRequestDetail",
            "type": "Element",
        },
    )
    order_request_summary: OrderRequestSummary | None = field(
        default=None,
        metadata={
            "name": "OrderRequestSummary",
            "type": "Element",
        },
    )
