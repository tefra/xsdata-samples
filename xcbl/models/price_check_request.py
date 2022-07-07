from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    Currency,
    Language,
    ListOfAttachment,
    ListOfDimension,
    Reference,
    Transport,
)
from xcbl.models.order_request import (
    AccountCode,
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
from xcbl.models.order_status_result import LineItemAttachment
from xcbl.models.payment_request_acknowledgment import SupplierParty
from xcbl.models.price_check_result import PriceCheckShipToParty


@dataclass
class PriceCheckRequestSummary:
    total_number_of_line_item: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalNumberOfLineItem",
            "type": "Element",
        }
    )


@dataclass
class PriceCheckRequestId:
    class Meta:
        name = "PriceCheckRequestID"

    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PriceCheckRequestLanguage:
    language: Optional[Language] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PriceCheckRequestTransport:
    transport: Optional[Transport] = field(
        default=None,
        metadata={
            "name": "Transport",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PriceCurrency:
    currency: Optional[Currency] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class RequestListOfAttachment:
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PriceCheckRequestBaseItemDetail:
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
    price_currency: Optional[PriceCurrency] = field(
        default=None,
        metadata={
            "name": "PriceCurrency",
            "type": "Element",
        }
    )
    price_check_request_transport: Optional[PriceCheckRequestTransport] = field(
        default=None,
        metadata={
            "name": "PriceCheckRequestTransport",
            "type": "Element",
        }
    )


@dataclass
class PriceCheckRequestHeader:
    price_check_request_id: Optional[PriceCheckRequestId] = field(
        default=None,
        metadata={
            "name": "PriceCheckRequestID",
            "type": "Element",
            "required": True,
        }
    )
    price_check_request_issue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "PriceCheckRequestIssueDate",
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
    account_code: Optional[AccountCode] = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Element",
        }
    )
    price_check_ship_to_party: Optional[PriceCheckShipToParty] = field(
        default=None,
        metadata={
            "name": "PriceCheckShipToParty",
            "type": "Element",
            "required": True,
        }
    )
    price_currency: Optional[PriceCurrency] = field(
        default=None,
        metadata={
            "name": "PriceCurrency",
            "type": "Element",
        }
    )
    quote_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "QuoteDate",
            "type": "Element",
        }
    )
    price_check_request_language: Optional[PriceCheckRequestLanguage] = field(
        default=None,
        metadata={
            "name": "PriceCheckRequestLanguage",
            "type": "Element",
        }
    )
    price_check_request_notes: Optional[str] = field(
        default=None,
        metadata={
            "name": "PriceCheckRequestNotes",
            "type": "Element",
        }
    )
    request_list_of_attachment: Optional[RequestListOfAttachment] = field(
        default=None,
        metadata={
            "name": "RequestListOfAttachment",
            "type": "Element",
        }
    )


@dataclass
class PriceCheckRequestItemDetail:
    price_check_request_base_item_detail: Optional[PriceCheckRequestBaseItemDetail] = field(
        default=None,
        metadata={
            "name": "PriceCheckRequestBaseItemDetail",
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
class ListOfPriceCheckRequestItemDetail:
    price_check_request_item_detail: List[PriceCheckRequestItemDetail] = field(
        default_factory=list,
        metadata={
            "name": "PriceCheckRequestItemDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class PriceCheckRequestDetail:
    list_of_price_check_request_item_detail: Optional[ListOfPriceCheckRequestItemDetail] = field(
        default=None,
        metadata={
            "name": "ListOfPriceCheckRequestItemDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PriceCheckRequest:
    price_check_request_header: Optional[PriceCheckRequestHeader] = field(
        default=None,
        metadata={
            "name": "PriceCheckRequestHeader",
            "type": "Element",
            "required": True,
        }
    )
    price_check_request_detail: Optional[PriceCheckRequestDetail] = field(
        default=None,
        metadata={
            "name": "PriceCheckRequestDetail",
            "type": "Element",
        }
    )
    price_check_request_summary: Optional[PriceCheckRequestSummary] = field(
        default=None,
        metadata={
            "name": "PriceCheckRequestSummary",
            "type": "Element",
        }
    )
