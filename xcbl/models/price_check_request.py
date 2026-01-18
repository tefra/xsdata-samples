from dataclasses import dataclass, field

from xcbl.models.price_check_result import (
    BuyerIdreferenceDate,
    GeneralLineItemNote,
    LineItemAttachment,
    PriceCheckShipToParty,
    QuoteDate,
    SupplierIdreferenceDate,
    TotalNumberOfLineItem,
)
from xcbl.models.remittance_advice import SupplierParty
from xcbl.models.shipping_schedule import AccountCode
from xcbl.models.sourcing_result import (
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
    ListOfAttachment,
    ListOfItemReferences,
    ListOfQuantityCoded,
    MaxBackOrderQuantity,
    OffCatalogFlag,
    ParentItemNumber,
    TotalQuantity,
    Transport,
)
from xcbl.models.time_series_response import (
    ListOfDimension,
    ListOfPartyCoded,
)
from xcbl.models.trading_partner_organization_information import Currency
from xcbl.models.trading_partner_response import Reference
from xcbl.models.trading_partner_user_information import Language


@dataclass(kw_only=True)
class PriceCheckRequestIssueDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PriceCheckRequestNotes:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PriceCheckRequestId:
    class Meta:
        name = "PriceCheckRequestID"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PriceCheckRequestLanguage:
    language: Language = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PriceCheckRequestSummary:
    total_number_of_line_item: TotalNumberOfLineItem | None = field(
        default=None,
        metadata={
            "name": "TotalNumberOfLineItem",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class PriceCheckRequestTransport:
    transport: Transport = field(
        metadata={
            "name": "Transport",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PriceCurrency:
    currency: Currency = field(
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RequestListOfAttachment:
    list_of_attachment: ListOfAttachment = field(
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PriceCheckRequestBaseItemDetail:
    line_item_num: LineItemNum = field(
        metadata={
            "name": "LineItemNum",
            "type": "Element",
            "required": True,
        }
    )
    line_item_type: LineItemType | None = field(
        default=None,
        metadata={
            "name": "LineItemType",
            "type": "Element",
        },
    )
    parent_item_number: ParentItemNumber | None = field(
        default=None,
        metadata={
            "name": "ParentItemNumber",
            "type": "Element",
        },
    )
    item_identifiers: ItemIdentifiers | None = field(
        default=None,
        metadata={
            "name": "ItemIdentifiers",
            "type": "Element",
        },
    )
    list_of_dimension: ListOfDimension | None = field(
        default=None,
        metadata={
            "name": "ListOfDimension",
            "type": "Element",
        },
    )
    total_quantity: TotalQuantity | None = field(
        default=None,
        metadata={
            "name": "TotalQuantity",
            "type": "Element",
        },
    )
    max_back_order_quantity: MaxBackOrderQuantity | None = field(
        default=None,
        metadata={
            "name": "MaxBackOrderQuantity",
            "type": "Element",
        },
    )
    list_of_quantity_coded: ListOfQuantityCoded | None = field(
        default=None,
        metadata={
            "name": "ListOfQuantityCoded",
            "type": "Element",
        },
    )
    off_catalog_flag: OffCatalogFlag | None = field(
        default=None,
        metadata={
            "name": "OffCatalogFlag",
            "type": "Element",
        },
    )
    catalog_reference: CatalogReference | None = field(
        default=None,
        metadata={
            "name": "CatalogReference",
            "type": "Element",
        },
    )
    item_contract_references: ItemContractReferences | None = field(
        default=None,
        metadata={
            "name": "ItemContractReferences",
            "type": "Element",
        },
    )
    list_of_item_references: ListOfItemReferences | None = field(
        default=None,
        metadata={
            "name": "ListOfItemReferences",
            "type": "Element",
        },
    )
    country_of_origin: CountryOfOrigin | None = field(
        default=None,
        metadata={
            "name": "CountryOfOrigin",
            "type": "Element",
        },
    )
    country_of_destination: CountryOfDestination | None = field(
        default=None,
        metadata={
            "name": "CountryOfDestination",
            "type": "Element",
        },
    )
    final_recipient: FinalRecipient | None = field(
        default=None,
        metadata={
            "name": "FinalRecipient",
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
    conditions_of_sale: ConditionsOfSale | None = field(
        default=None,
        metadata={
            "name": "ConditionsOfSale",
            "type": "Element",
        },
    )
    hazardous_materials: HazardousMaterials | None = field(
        default=None,
        metadata={
            "name": "HazardousMaterials",
            "type": "Element",
        },
    )
    price_currency: PriceCurrency | None = field(
        default=None,
        metadata={
            "name": "PriceCurrency",
            "type": "Element",
        },
    )
    price_check_request_transport: PriceCheckRequestTransport | None = field(
        default=None,
        metadata={
            "name": "PriceCheckRequestTransport",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class PriceCheckRequestHeader:
    price_check_request_id: PriceCheckRequestId = field(
        metadata={
            "name": "PriceCheckRequestID",
            "type": "Element",
            "required": True,
        }
    )
    price_check_request_issue_date: PriceCheckRequestIssueDate = field(
        metadata={
            "name": "PriceCheckRequestIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    supplier_party: SupplierParty = field(
        metadata={
            "name": "SupplierParty",
            "type": "Element",
            "required": True,
        }
    )
    supplier_idreference_date: SupplierIdreferenceDate | None = field(
        default=None,
        metadata={
            "name": "SupplierIDReferenceDate",
            "type": "Element",
        },
    )
    buyer_party: BuyerParty = field(
        metadata={
            "name": "BuyerParty",
            "type": "Element",
            "required": True,
        }
    )
    buyer_idreference_date: BuyerIdreferenceDate | None = field(
        default=None,
        metadata={
            "name": "BuyerIDReferenceDate",
            "type": "Element",
        },
    )
    account_code: AccountCode | None = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Element",
        },
    )
    price_check_ship_to_party: PriceCheckShipToParty = field(
        metadata={
            "name": "PriceCheckShipToParty",
            "type": "Element",
            "required": True,
        }
    )
    price_currency: PriceCurrency | None = field(
        default=None,
        metadata={
            "name": "PriceCurrency",
            "type": "Element",
        },
    )
    quote_date: QuoteDate | None = field(
        default=None,
        metadata={
            "name": "QuoteDate",
            "type": "Element",
        },
    )
    price_check_request_language: PriceCheckRequestLanguage | None = field(
        default=None,
        metadata={
            "name": "PriceCheckRequestLanguage",
            "type": "Element",
        },
    )
    price_check_request_notes: PriceCheckRequestNotes | None = field(
        default=None,
        metadata={
            "name": "PriceCheckRequestNotes",
            "type": "Element",
        },
    )
    request_list_of_attachment: RequestListOfAttachment | None = field(
        default=None,
        metadata={
            "name": "RequestListOfAttachment",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class PriceCheckRequestItemDetail:
    price_check_request_base_item_detail: PriceCheckRequestBaseItemDetail = (
        field(
            metadata={
                "name": "PriceCheckRequestBaseItemDetail",
                "type": "Element",
                "required": True,
            }
        )
    )
    general_line_item_note: GeneralLineItemNote | None = field(
        default=None,
        metadata={
            "name": "GeneralLineItemNote",
            "type": "Element",
        },
    )
    line_item_attachment: LineItemAttachment | None = field(
        default=None,
        metadata={
            "name": "LineItemAttachment",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfPriceCheckRequestItemDetail:
    price_check_request_item_detail: list[PriceCheckRequestItemDetail] = field(
        default_factory=list,
        metadata={
            "name": "PriceCheckRequestItemDetail",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class PriceCheckRequestDetail:
    list_of_price_check_request_item_detail: ListOfPriceCheckRequestItemDetail = field(
        metadata={
            "name": "ListOfPriceCheckRequestItemDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PriceCheckRequest:
    price_check_request_header: PriceCheckRequestHeader = field(
        metadata={
            "name": "PriceCheckRequestHeader",
            "type": "Element",
            "required": True,
        }
    )
    price_check_request_detail: PriceCheckRequestDetail | None = field(
        default=None,
        metadata={
            "name": "PriceCheckRequestDetail",
            "type": "Element",
        },
    )
    price_check_request_summary: PriceCheckRequestSummary | None = field(
        default=None,
        metadata={
            "name": "PriceCheckRequestSummary",
            "type": "Element",
        },
    )
