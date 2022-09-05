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


@dataclass(kw_only=True)
class RequestQuotePurpose:
    request_quote_purpose_coded: str = field(
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


@dataclass(kw_only=True)
class RequestQuoteSummary:
    total_number_of_line_items: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalNumberOfLineItems",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class AccountNumber:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class BuyersCatalogNumber:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ContractReference:
    contract: Contract = field(
        metadata={
            "name": "Contract",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfRequestQuotePackageDetail:
    list_of_package_detail: ListOfPackageDetail = field(
        metadata={
            "name": "ListOfPackageDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ManufacturingToParty:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class MaterialIssuer:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OtherRequestQuoteReferences:
    list_of_reference_coded: ListOfReferenceCoded = field(
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PriceListNumber:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PriceListVersionNumber:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RequestQuoteAllowanceOrCharge:
    list_of_allow_or_charge: ListOfAllowOrCharge = field(
        metadata={
            "name": "ListOfAllowOrCharge",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RequestQuoteCurrency:
    currency: Currency = field(
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RequestQuoteDeliveryDetail:
    delivery_detail: DeliveryDetail = field(
        metadata={
            "name": "DeliveryDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RequestQuoteId:
    class Meta:
        name = "RequestQuoteID"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RequestQuoteItemDetail:
    base_item_detail: BaseItemDetail = field(
        metadata={
            "name": "BaseItemDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RequestQuoteItemListOfAttachment:
    list_of_attachment: ListOfAttachment = field(
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RequestQuoteLanguage:
    language: Language = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RequestQuoteListOfAttachment:
    list_of_attachment: ListOfAttachment = field(
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RequestQuotePricingDetail:
    pricing_detail: PricingDetail = field(
        metadata={
            "name": "PricingDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RequestQuoteTax:
    tax: Tax = field(
        metadata={
            "name": "Tax",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RequestQuoteTermsOfDelivery:
    terms_of_delivery: TermsOfDelivery = field(
        metadata={
            "name": "TermsOfDelivery",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RequestQuoteTermsOfPayment:
    payment_instructions: PaymentInstructions = field(
        metadata={
            "name": "PaymentInstructions",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RequestQuoteTransport:
    transport_routing: TransportRouting = field(
        metadata={
            "name": "TransportRouting",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RequestQuoteValidityDate:
    validity_dates: ValidityDates = field(
        metadata={
            "name": "ValidityDates",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ResultingOrderType:
    order_type: OrderType = field(
        metadata={
            "name": "OrderType",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SoldToParty:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class WarehouseParty:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderParty:
    buyer_party: BuyerParty = field(
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


@dataclass(kw_only=True)
class RequestQuoteDate:
    request_quote_validity_date: RequestQuoteValidityDate = field(
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


@dataclass(kw_only=True)
class RequestQuoteDetails:
    request_quote_item_detail: RequestQuoteItemDetail = field(
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


@dataclass(kw_only=True)
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


@dataclass(kw_only=True)
class ListOfRequestQuoteDetails:
    request_quote_details: List[RequestQuoteDetails] = field(
        default_factory=list,
        metadata={
            "name": "RequestQuoteDetails",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class RequestQuoteParty:
    order_party: OrderParty = field(
        metadata={
            "name": "OrderParty",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RequestQuoteHeader:
    request_quote_issue_date: str = field(
        metadata={
            "name": "RequestQuoteIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    request_quote_id: RequestQuoteId = field(
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
    request_quote_party: RequestQuoteParty = field(
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


@dataclass(kw_only=True)
class RequestForQuotation:
    request_quote_header: RequestQuoteHeader = field(
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
