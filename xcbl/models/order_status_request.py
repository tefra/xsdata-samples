from dataclasses import dataclass, field
from typing import List, Optional

from xcbl.models.order_status_result import (
    BuyerReferenceNumber,
    OrderDate,
    OrderStatusIssueDate,
    OtherReference,
    SellerReferenceNumber,
    VarianceQty,
)
from xcbl.models.price_check_result import (
    GeneralLineItemNote,
    LineItemAttachment,
    TotalNumberOfLineItem,
)
from xcbl.models.shipping_schedule import AccountCode
from xcbl.models.sourcing_result import (
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
    OrderParty,
    ParentItemNumber,
    TotalQuantity,
    Transport,
)
from xcbl.models.time_series_response import (
    ListOfDimension,
    ListOfPartyCoded,
)
from xcbl.models.trading_partner_response import Reference
from xcbl.models.trading_partner_user_information import Language


@dataclass(kw_only=True)
class OrderStatusRequestNote:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class OrderStatusItemTransport:
    transport: Transport = field(
        metadata={
            "name": "Transport",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderStatusLanguage:
    language: Language = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderStatusListOfAttachment:
    list_of_attachment: ListOfAttachment = field(
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderStatusParty:
    order_party: OrderParty = field(
        metadata={
            "name": "OrderParty",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderStatusRequestId:
    class Meta:
        name = "OrderStatusRequestID"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderStatusRequestSummary:
    total_number_of_line_item: Optional[TotalNumberOfLineItem] = field(
        default=None,
        metadata={
            "name": "TotalNumberOfLineItem",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class OrderStatusItem:
    line_item_num: LineItemNum = field(
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
        },
    )
    parent_item_number: Optional[ParentItemNumber] = field(
        default=None,
        metadata={
            "name": "ParentItemNumber",
            "type": "Element",
        },
    )
    item_identifiers: Optional[ItemIdentifiers] = field(
        default=None,
        metadata={
            "name": "ItemIdentifiers",
            "type": "Element",
        },
    )
    list_of_dimension: Optional[ListOfDimension] = field(
        default=None,
        metadata={
            "name": "ListOfDimension",
            "type": "Element",
        },
    )
    total_quantity: Optional[TotalQuantity] = field(
        default=None,
        metadata={
            "name": "TotalQuantity",
            "type": "Element",
        },
    )
    max_back_order_quantity: Optional[MaxBackOrderQuantity] = field(
        default=None,
        metadata={
            "name": "MaxBackOrderQuantity",
            "type": "Element",
        },
    )
    list_of_quantity_coded: Optional[ListOfQuantityCoded] = field(
        default=None,
        metadata={
            "name": "ListOfQuantityCoded",
            "type": "Element",
        },
    )
    off_catalog_flag: Optional[OffCatalogFlag] = field(
        default=None,
        metadata={
            "name": "OffCatalogFlag",
            "type": "Element",
        },
    )
    catalog_reference: Optional[CatalogReference] = field(
        default=None,
        metadata={
            "name": "CatalogReference",
            "type": "Element",
        },
    )
    item_contract_references: Optional[ItemContractReferences] = field(
        default=None,
        metadata={
            "name": "ItemContractReferences",
            "type": "Element",
        },
    )
    list_of_item_references: Optional[ListOfItemReferences] = field(
        default=None,
        metadata={
            "name": "ListOfItemReferences",
            "type": "Element",
        },
    )
    country_of_origin: Optional[CountryOfOrigin] = field(
        default=None,
        metadata={
            "name": "CountryOfOrigin",
            "type": "Element",
        },
    )
    country_of_destination: Optional[CountryOfDestination] = field(
        default=None,
        metadata={
            "name": "CountryOfDestination",
            "type": "Element",
        },
    )
    final_recipient: Optional[FinalRecipient] = field(
        default=None,
        metadata={
            "name": "FinalRecipient",
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
    conditions_of_sale: Optional[ConditionsOfSale] = field(
        default=None,
        metadata={
            "name": "ConditionsOfSale",
            "type": "Element",
        },
    )
    hazardous_materials: Optional[HazardousMaterials] = field(
        default=None,
        metadata={
            "name": "HazardousMaterials",
            "type": "Element",
        },
    )
    order_status_item_transport: Optional[OrderStatusItemTransport] = field(
        default=None,
        metadata={
            "name": "OrderStatusItemTransport",
            "type": "Element",
        },
    )
    variance_qty: VarianceQty = field(
        metadata={
            "name": "VarianceQty",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderStatusRequestHeader:
    order_status_request_id: OrderStatusRequestId = field(
        metadata={
            "name": "OrderStatusRequestID",
            "type": "Element",
            "required": True,
        }
    )
    order_status_issue_date: OrderStatusIssueDate = field(
        metadata={
            "name": "OrderStatusIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    order_status_party: OrderStatusParty = field(
        metadata={
            "name": "OrderStatusParty",
            "type": "Element",
            "required": True,
        }
    )
    order_status_language: Optional[OrderStatusLanguage] = field(
        default=None,
        metadata={
            "name": "OrderStatusLanguage",
            "type": "Element",
        },
    )
    order_status_request_note: Optional[OrderStatusRequestNote] = field(
        default=None,
        metadata={
            "name": "OrderStatusRequestNote",
            "type": "Element",
        },
    )
    order_status_list_of_attachment: Optional[OrderStatusListOfAttachment] = (
        field(
            default=None,
            metadata={
                "name": "OrderStatusListOfAttachment",
                "type": "Element",
            },
        )
    )


@dataclass(kw_only=True)
class ListOfOrderStatusItem:
    order_status_item: List[OrderStatusItem] = field(
        default_factory=list,
        metadata={
            "name": "OrderStatusItem",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class OrderStatusReference:
    account_code: Optional[AccountCode] = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Element",
        },
    )
    buyer_reference_number: BuyerReferenceNumber = field(
        metadata={
            "name": "BuyerReferenceNumber",
            "type": "Element",
            "required": True,
        }
    )
    seller_reference_number: SellerReferenceNumber = field(
        metadata={
            "name": "SellerReferenceNumber",
            "type": "Element",
            "required": True,
        }
    )
    other_reference: Optional[OtherReference] = field(
        default=None,
        metadata={
            "name": "OtherReference",
            "type": "Element",
        },
    )
    order_date: OrderDate = field(
        metadata={
            "name": "OrderDate",
            "type": "Element",
            "required": True,
        }
    )
    list_of_order_status_item: Optional[ListOfOrderStatusItem] = field(
        default=None,
        metadata={
            "name": "ListOfOrderStatusItem",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class OrderStatusDetailRequest:
    order_status_reference: OrderStatusReference = field(
        metadata={
            "name": "OrderStatusReference",
            "type": "Element",
            "required": True,
        }
    )
    general_line_item_note: Optional[GeneralLineItemNote] = field(
        default=None,
        metadata={
            "name": "GeneralLineItemNote",
            "type": "Element",
        },
    )
    line_item_attachment: Optional[LineItemAttachment] = field(
        default=None,
        metadata={
            "name": "LineItemAttachment",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfOrderStatusRequestDetail:
    order_status_detail_request: List[OrderStatusDetailRequest] = field(
        default_factory=list,
        metadata={
            "name": "OrderStatusDetailRequest",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class OrderStatusRequestDetail:
    list_of_order_status_request_detail: ListOfOrderStatusRequestDetail = (
        field(
            metadata={
                "name": "ListOfOrderStatusRequestDetail",
                "type": "Element",
                "required": True,
            }
        )
    )


@dataclass(kw_only=True)
class OrderStatusRequest:
    order_status_request_header: OrderStatusRequestHeader = field(
        metadata={
            "name": "OrderStatusRequestHeader",
            "type": "Element",
            "required": True,
        }
    )
    order_status_request_detail: Optional[OrderStatusRequestDetail] = field(
        default=None,
        metadata={
            "name": "OrderStatusRequestDetail",
            "type": "Element",
        },
    )
    order_status_request_summary: Optional[OrderStatusRequestSummary] = field(
        default=None,
        metadata={
            "name": "OrderStatusRequestSummary",
            "type": "Element",
        },
    )
