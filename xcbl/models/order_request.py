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
    seller_order_request_number: None | SellerOrderRequestNumber = field(
        default=None,
        metadata={
            "name": "SellerOrderRequestNumber",
            "type": "Element",
        },
    )
    list_of_message_id: None | ListOfMessageId = field(
        default=None,
        metadata={
            "name": "ListOfMessageID",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class OrderRequestParty:
    buyer_party: None | BuyerParty = field(
        default=None,
        metadata={
            "name": "BuyerParty",
            "type": "Element",
        },
    )
    buyer_tax_information: None | BuyerTaxInformation = field(
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
    seller_tax_information: None | SellerTaxInformation = field(
        default=None,
        metadata={
            "name": "SellerTaxInformation",
            "type": "Element",
        },
    )
    ship_to_party: None | ShipToParty = field(
        default=None,
        metadata={
            "name": "ShipToParty",
            "type": "Element",
        },
    )
    bill_to_party: None | BillToParty = field(
        default=None,
        metadata={
            "name": "BillToParty",
            "type": "Element",
        },
    )
    remit_to_party: None | RemitToParty = field(
        default=None,
        metadata={
            "name": "RemitToParty",
            "type": "Element",
        },
    )
    ship_from_party: None | ShipFromParty = field(
        default=None,
        metadata={
            "name": "ShipFromParty",
            "type": "Element",
        },
    )
    list_of_party_coded: None | ListOfPartyCoded = field(
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
    list_of_package_detail: None | ListOfPackageDetail = field(
        default=None,
        metadata={
            "name": "ListOfPackageDetail",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class OrderRequestHeader:
    order_request_number: None | OrderRequestNumber = field(
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
    order_request_references: None | OrderRequestReferences = field(
        default=None,
        metadata={
            "name": "OrderRequestReferences",
            "type": "Element",
        },
    )
    purpose: None | Purpose = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Element",
        },
    )
    requested_response: None | RequestedResponse = field(
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
    tax_accounting_currency: None | TaxAccountingCurrency = field(
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
    order_request_tax_reference: None | OrderRequestTaxReference = field(
        default=None,
        metadata={
            "name": "OrderRequestTaxReference",
            "type": "Element",
        },
    )
    order_invoice_medium_type_coded: None | OrderInvoiceMediumTypeCoded = (
        field(
            default=None,
            metadata={
                "name": "OrderInvoiceMediumTypeCoded",
                "type": "Element",
            },
        )
    )
    order_invoice_medium_type_coded_other: (
        None | OrderInvoiceMediumTypeCodedOther
    ) = field(
        default=None,
        metadata={
            "name": "OrderInvoiceMediumTypeCodedOther",
            "type": "Element",
        },
    )
    order_request_dates: None | OrderRequestDates = field(
        default=None,
        metadata={
            "name": "OrderRequestDates",
            "type": "Element",
        },
    )
    partial_shipment_allowed: None | PartialShipmentAllowed = field(
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
    list_of_transport: None | ListOfTransport = field(
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
    order_header_price: None | OrderHeaderPrice = field(
        default=None,
        metadata={
            "name": "OrderHeaderPrice",
            "type": "Element",
        },
    )
    order_payment_instructions: None | OrderPaymentInstructions = field(
        default=None,
        metadata={
            "name": "OrderPaymentInstructions",
            "type": "Element",
        },
    )
    order_allowances_or_charges: None | OrderAllowancesOrCharges = field(
        default=None,
        metadata={
            "name": "OrderAllowancesOrCharges",
            "type": "Element",
        },
    )
    round_trip_information: None | RoundTripInformation = field(
        default=None,
        metadata={
            "name": "RoundTripInformation",
            "type": "Element",
        },
    )
    order_header_note: None | OrderHeaderNote = field(
        default=None,
        metadata={
            "name": "OrderHeaderNote",
            "type": "Element",
        },
    )
    list_of_structured_note: None | ListOfStructuredNote = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        },
    )
    order_header_attachments: None | OrderHeaderAttachments = field(
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
    order_request_detail: None | OrderRequestDetail = field(
        default=None,
        metadata={
            "name": "OrderRequestDetail",
            "type": "Element",
        },
    )
    order_request_summary: None | OrderRequestSummary = field(
        default=None,
        metadata={
            "name": "OrderRequestSummary",
            "type": "Element",
        },
    )
