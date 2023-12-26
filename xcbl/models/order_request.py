from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.order_response import (
    ListOfTransport,
    OrderAllowancesOrCharges,
    OrderHeaderAttachments,
    OrderHeaderPrice,
    OrderPaymentInstructions,
    OrderSummary,
    OrderTermsOfDelivery,
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
class ListOfItemDetail:
    item_detail: List[ItemDetail] = field(
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
    buyer_order_request_number: str = field(
        metadata={
            "name": "BuyerOrderRequestNumber",
            "type": "Element",
            "required": True,
        }
    )
    seller_order_request_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SellerOrderRequestNumber",
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
class OrderRequestParty:
    buyer_party: Optional[BuyerParty] = field(
        default=None,
        metadata={
            "name": "BuyerParty",
            "type": "Element",
        },
    )
    buyer_tax_information: Optional[BuyerTaxInformation] = field(
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
    seller_tax_information: Optional[SellerTaxInformation] = field(
        default=None,
        metadata={
            "name": "SellerTaxInformation",
            "type": "Element",
        },
    )
    ship_to_party: Optional[ShipToParty] = field(
        default=None,
        metadata={
            "name": "ShipToParty",
            "type": "Element",
        },
    )
    bill_to_party: Optional[BillToParty] = field(
        default=None,
        metadata={
            "name": "BillToParty",
            "type": "Element",
        },
    )
    remit_to_party: Optional[RemitToParty] = field(
        default=None,
        metadata={
            "name": "RemitToParty",
            "type": "Element",
        },
    )
    ship_from_party: Optional[ShipFromParty] = field(
        default=None,
        metadata={
            "name": "ShipFromParty",
            "type": "Element",
        },
    )
    list_of_party_coded: Optional[ListOfPartyCoded] = field(
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
    list_of_package_detail: Optional[ListOfPackageDetail] = field(
        default=None,
        metadata={
            "name": "ListOfPackageDetail",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class OrderRequestHeader:
    order_request_number: Optional[OrderRequestNumber] = field(
        default=None,
        metadata={
            "name": "OrderRequestNumber",
            "type": "Element",
        },
    )
    order_request_issue_date: str = field(
        metadata={
            "name": "OrderRequestIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    order_request_references: Optional[OrderRequestReferences] = field(
        default=None,
        metadata={
            "name": "OrderRequestReferences",
            "type": "Element",
        },
    )
    purpose: Optional[Purpose] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Element",
        },
    )
    requested_response: Optional[RequestedResponse] = field(
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
    tax_accounting_currency: Optional[TaxAccountingCurrency] = field(
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
    order_request_tax_reference: Optional[OrderRequestTaxReference] = field(
        default=None,
        metadata={
            "name": "OrderRequestTaxReference",
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
    order_request_dates: Optional[OrderRequestDates] = field(
        default=None,
        metadata={
            "name": "OrderRequestDates",
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
    order_request_party: OrderRequestParty = field(
        metadata={
            "name": "OrderRequestParty",
            "type": "Element",
            "required": True,
        }
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
    order_header_attachments: Optional[OrderHeaderAttachments] = field(
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
    order_request_detail: Optional[OrderRequestDetail] = field(
        default=None,
        metadata={
            "name": "OrderRequestDetail",
            "type": "Element",
        },
    )
    order_request_summary: Optional[OrderRequestSummary] = field(
        default=None,
        metadata={
            "name": "OrderRequestSummary",
            "type": "Element",
        },
    )
