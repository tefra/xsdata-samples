from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    Currency,
    DeliveryDetail,
    Language,
    ListOfAttachment,
    ListOfReferenceCoded,
    Party,
    Reference,
    TermsOfDelivery,
    ValidityDates,
)
from xcbl.models.goods_receipt import TransportRouting
from xcbl.models.order_request import (
    BaseItemDetail,
    BillToParty,
    BuyerParty,
    BuyerTaxInformation,
    Contract,
    ListOfAllowOrCharge,
    ListOfPackageDetail,
    ListOfPartyCoded,
    PaymentInstructions,
    PricingDetail,
    RemitToParty,
    SellerParty,
    SellerTaxInformation,
    ShipFromParty,
    ShipToParty,
    Tax,
)
from xcbl.models.planning_schedule import OrderType


@dataclass
class RequestQuotePurpose:
    request_quote_purpose_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestQuotePurposeCoded",
            "type": "Element",
            "required": True,
        }
    )
    request_quote_purpose_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestQuotePurposeCodedOther",
            "type": "Element",
        }
    )


@dataclass
class RequestQuoteSummary:
    total_number_of_line_items: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalNumberOfLineItems",
            "type": "Element",
        }
    )


@dataclass
class AccountNumber:
    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class BuyersCatalogNumber:
    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ContractReference:
    contract: Optional[Contract] = field(
        default=None,
        metadata={
            "name": "Contract",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfRequestQuotePackageDetail:
    list_of_package_detail: Optional[ListOfPackageDetail] = field(
        default=None,
        metadata={
            "name": "ListOfPackageDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ManufacturingToParty:
    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class MaterialIssuer:
    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OtherRequestQuoteReferences:
    list_of_reference_coded: Optional[ListOfReferenceCoded] = field(
        default=None,
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PriceListNumber:
    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PriceListVersionNumber:
    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class RequestQuoteAllowanceOrCharge:
    list_of_allow_or_charge: Optional[ListOfAllowOrCharge] = field(
        default=None,
        metadata={
            "name": "ListOfAllowOrCharge",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class RequestQuoteCurrency:
    currency: Optional[Currency] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class RequestQuoteDeliveryDetail:
    delivery_detail: Optional[DeliveryDetail] = field(
        default=None,
        metadata={
            "name": "DeliveryDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class RequestQuoteId:
    class Meta:
        name = "RequestQuoteID"

    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class RequestQuoteItemDetail:
    base_item_detail: Optional[BaseItemDetail] = field(
        default=None,
        metadata={
            "name": "BaseItemDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class RequestQuoteItemListOfAttachment:
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class RequestQuoteLanguage:
    language: Optional[Language] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class RequestQuoteListOfAttachment:
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class RequestQuotePricingDetail:
    pricing_detail: Optional[PricingDetail] = field(
        default=None,
        metadata={
            "name": "PricingDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class RequestQuoteTax:
    tax: Optional[Tax] = field(
        default=None,
        metadata={
            "name": "Tax",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class RequestQuoteTermsOfDelivery:
    terms_of_delivery: Optional[TermsOfDelivery] = field(
        default=None,
        metadata={
            "name": "TermsOfDelivery",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class RequestQuoteTermsOfPayment:
    payment_instructions: Optional[PaymentInstructions] = field(
        default=None,
        metadata={
            "name": "PaymentInstructions",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class RequestQuoteTransport:
    transport_routing: Optional[TransportRouting] = field(
        default=None,
        metadata={
            "name": "TransportRouting",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class RequestQuoteValidityDate:
    validity_dates: Optional[ValidityDates] = field(
        default=None,
        metadata={
            "name": "ValidityDates",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ResultingOrderType:
    order_type: Optional[OrderType] = field(
        default=None,
        metadata={
            "name": "OrderType",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SoldToParty:
    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class WarehouseParty:
    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OrderParty:
    buyer_party: Optional[BuyerParty] = field(
        default=None,
        metadata={
            "name": "BuyerParty",
            "type": "Element",
            "required": True,
        }
    )
    buyer_tax_information: Optional[BuyerTaxInformation] = field(
        default=None,
        metadata={
            "name": "BuyerTaxInformation",
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
    seller_tax_information: Optional[SellerTaxInformation] = field(
        default=None,
        metadata={
            "name": "SellerTaxInformation",
            "type": "Element",
        }
    )
    ship_to_party: Optional[ShipToParty] = field(
        default=None,
        metadata={
            "name": "ShipToParty",
            "type": "Element",
        }
    )
    bill_to_party: Optional[BillToParty] = field(
        default=None,
        metadata={
            "name": "BillToParty",
            "type": "Element",
        }
    )
    remit_to_party: Optional[RemitToParty] = field(
        default=None,
        metadata={
            "name": "RemitToParty",
            "type": "Element",
        }
    )
    ship_from_party: Optional[ShipFromParty] = field(
        default=None,
        metadata={
            "name": "ShipFromParty",
            "type": "Element",
        }
    )
    warehouse_party: Optional[WarehouseParty] = field(
        default=None,
        metadata={
            "name": "WarehouseParty",
            "type": "Element",
        }
    )
    sold_to_party: Optional[SoldToParty] = field(
        default=None,
        metadata={
            "name": "SoldToParty",
            "type": "Element",
        }
    )
    manufacturing_to_party: Optional[ManufacturingToParty] = field(
        default=None,
        metadata={
            "name": "ManufacturingToParty",
            "type": "Element",
        }
    )
    material_issuer: Optional[MaterialIssuer] = field(
        default=None,
        metadata={
            "name": "MaterialIssuer",
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
class RequestQuoteDate:
    request_quote_validity_date: Optional[RequestQuoteValidityDate] = field(
        default=None,
        metadata={
            "name": "RequestQuoteValidityDate",
            "type": "Element",
            "required": True,
        }
    )
    decision_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "DecisionDate",
            "type": "Element",
        }
    )
    delivery_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "DeliveryDate",
            "type": "Element",
        }
    )
    delivery_date_earliest: Optional[str] = field(
        default=None,
        metadata={
            "name": "DeliveryDateEarliest",
            "type": "Element",
        }
    )
    delivery_date_latest: Optional[str] = field(
        default=None,
        metadata={
            "name": "DeliveryDateLatest",
            "type": "Element",
        }
    )
    advise_before: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdviseBefore",
            "type": "Element",
        }
    )
    cancel_if_not_delivered: Optional[str] = field(
        default=None,
        metadata={
            "name": "CancelIfNotDelivered",
            "type": "Element",
        }
    )


@dataclass
class RequestQuoteDetails:
    request_quote_item_detail: Optional[RequestQuoteItemDetail] = field(
        default=None,
        metadata={
            "name": "RequestQuoteItemDetail",
            "type": "Element",
            "required": True,
        }
    )
    request_quote_pricing_detail: Optional[RequestQuotePricingDetail] = field(
        default=None,
        metadata={
            "name": "RequestQuotePricingDetail",
            "type": "Element",
        }
    )
    request_quote_delivery_detail: Optional[RequestQuoteDeliveryDetail] = field(
        default=None,
        metadata={
            "name": "RequestQuoteDeliveryDetail",
            "type": "Element",
        }
    )
    request_quote_item_list_of_attachment: Optional[RequestQuoteItemListOfAttachment] = field(
        default=None,
        metadata={
            "name": "RequestQuoteItemListOfAttachment",
            "type": "Element",
        }
    )


@dataclass
class RequestQuoteReference:
    contract_reference: Optional[ContractReference] = field(
        default=None,
        metadata={
            "name": "ContractReference",
            "type": "Element",
        }
    )
    account_number: Optional[AccountNumber] = field(
        default=None,
        metadata={
            "name": "AccountNumber",
            "type": "Element",
        }
    )
    price_list_number: Optional[PriceListNumber] = field(
        default=None,
        metadata={
            "name": "PriceListNumber",
            "type": "Element",
        }
    )
    price_list_version_number: Optional[PriceListVersionNumber] = field(
        default=None,
        metadata={
            "name": "PriceListVersionNumber",
            "type": "Element",
        }
    )
    buyers_catalog_number: Optional[BuyersCatalogNumber] = field(
        default=None,
        metadata={
            "name": "BuyersCatalogNumber",
            "type": "Element",
        }
    )
    other_request_quote_references: Optional[OtherRequestQuoteReferences] = field(
        default=None,
        metadata={
            "name": "OtherRequestQuoteReferences",
            "type": "Element",
        }
    )


@dataclass
class ListOfRequestQuoteDetails:
    request_quote_details: List[RequestQuoteDetails] = field(
        default_factory=list,
        metadata={
            "name": "RequestQuoteDetails",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class RequestQuoteParty:
    order_party: Optional[OrderParty] = field(
        default=None,
        metadata={
            "name": "OrderParty",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class RequestQuoteHeader:
    request_quote_issue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestQuoteIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    request_quote_id: Optional[RequestQuoteId] = field(
        default=None,
        metadata={
            "name": "RequestQuoteID",
            "type": "Element",
            "required": True,
        }
    )
    request_quote_reference: Optional[RequestQuoteReference] = field(
        default=None,
        metadata={
            "name": "RequestQuoteReference",
            "type": "Element",
        }
    )
    request_quote_purpose: Optional[RequestQuotePurpose] = field(
        default=None,
        metadata={
            "name": "RequestQuotePurpose",
            "type": "Element",
        }
    )
    request_quote_date: Optional[RequestQuoteDate] = field(
        default=None,
        metadata={
            "name": "RequestQuoteDate",
            "type": "Element",
        }
    )
    request_quote_party: Optional[RequestQuoteParty] = field(
        default=None,
        metadata={
            "name": "RequestQuoteParty",
            "type": "Element",
            "required": True,
        }
    )
    resulting_order_type: Optional[ResultingOrderType] = field(
        default=None,
        metadata={
            "name": "ResultingOrderType",
            "type": "Element",
        }
    )
    request_quote_currency: Optional[RequestQuoteCurrency] = field(
        default=None,
        metadata={
            "name": "RequestQuoteCurrency",
            "type": "Element",
        }
    )
    request_quote_allowance_or_charge: Optional[RequestQuoteAllowanceOrCharge] = field(
        default=None,
        metadata={
            "name": "RequestQuoteAllowanceOrCharge",
            "type": "Element",
        }
    )
    request_quote_terms_of_payment: Optional[RequestQuoteTermsOfPayment] = field(
        default=None,
        metadata={
            "name": "RequestQuoteTermsOfPayment",
            "type": "Element",
        }
    )
    request_quote_terms_of_delivery: Optional[RequestQuoteTermsOfDelivery] = field(
        default=None,
        metadata={
            "name": "RequestQuoteTermsOfDelivery",
            "type": "Element",
        }
    )
    request_quote_tax: Optional[RequestQuoteTax] = field(
        default=None,
        metadata={
            "name": "RequestQuoteTax",
            "type": "Element",
        }
    )
    request_quote_transport: Optional[RequestQuoteTransport] = field(
        default=None,
        metadata={
            "name": "RequestQuoteTransport",
            "type": "Element",
        }
    )
    request_quote_language: Optional[RequestQuoteLanguage] = field(
        default=None,
        metadata={
            "name": "RequestQuoteLanguage",
            "type": "Element",
        }
    )
    request_quote_general_notes: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestQuoteGeneralNotes",
            "type": "Element",
        }
    )
    request_quote_list_of_attachment: Optional[RequestQuoteListOfAttachment] = field(
        default=None,
        metadata={
            "name": "RequestQuoteListOfAttachment",
            "type": "Element",
        }
    )


@dataclass
class RequestForQuotation:
    request_quote_header: Optional[RequestQuoteHeader] = field(
        default=None,
        metadata={
            "name": "RequestQuoteHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_request_quote_details: Optional[ListOfRequestQuoteDetails] = field(
        default=None,
        metadata={
            "name": "ListOfRequestQuoteDetails",
            "type": "Element",
        }
    )
    list_of_request_quote_package_detail: Optional[ListOfRequestQuotePackageDetail] = field(
        default=None,
        metadata={
            "name": "ListOfRequestQuotePackageDetail",
            "type": "Element",
        }
    )
    request_quote_summary: Optional[RequestQuoteSummary] = field(
        default=None,
        metadata={
            "name": "RequestQuoteSummary",
            "type": "Element",
        }
    )
