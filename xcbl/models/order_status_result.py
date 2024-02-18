from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.price_check_result import (
    ErrorInfo,
    GeneralLineItemNote,
    LineItemAttachment,
    ResultListOfAttachment,
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
    ListOfItemReferences,
    ListOfQuantityCoded,
    ListOfReferenceCoded,
    ListOfStatusReason,
    MaxBackOrderQuantity,
    OffCatalogFlag,
    OrderParty,
    ParentItemNumber,
    Quantity,
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
class OrderDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class OrderStatusCheckItemError:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class OrderStatusDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class OrderStatusIssueDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class OrderStatusResultNote:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ShipDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class StatusEventCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class StatusEventCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class StatusNote:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class BuyerReferenceNumber:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ItemStatusQuantity:
    quantity: Quantity = field(
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderStatusId:
    class Meta:
        name = "OrderStatusID"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderStatusItemResultTransport:
    transport: Transport = field(
        metadata={
            "name": "Transport",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderStatusResultLanguage:
    language: Language = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderStatusResultParty:
    order_party: OrderParty = field(
        metadata={
            "name": "OrderParty",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderStatusSummaryErrorInfo:
    error_info: ErrorInfo = field(
        metadata={
            "name": "ErrorInfo",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OtherReference:
    list_of_reference_coded: ListOfReferenceCoded = field(
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SellerReferenceNumber:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class StatusEvent:
    status_event_coded: StatusEventCoded = field(
        metadata={
            "name": "StatusEventCoded",
            "type": "Element",
            "required": True,
        }
    )
    status_event_coded_other: Optional[StatusEventCodedOther] = field(
        default=None,
        metadata={
            "name": "StatusEventCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class VarianceQty:
    quantity: Quantity = field(
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderStatusResultHeader:
    order_status_id: OrderStatusId = field(
        metadata={
            "name": "OrderStatusID",
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
    order_status_result_party: OrderStatusResultParty = field(
        metadata={
            "name": "OrderStatusResultParty",
            "type": "Element",
            "required": True,
        }
    )
    order_status_result_language: Optional[OrderStatusResultLanguage] = field(
        default=None,
        metadata={
            "name": "OrderStatusResultLanguage",
            "type": "Element",
        },
    )
    order_status_result_note: Optional[OrderStatusResultNote] = field(
        default=None,
        metadata={
            "name": "OrderStatusResultNote",
            "type": "Element",
        },
    )
    result_list_of_attachment: Optional[ResultListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ResultListOfAttachment",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class OrderStatusResultSummary:
    order_status_check_item_error: OrderStatusCheckItemError = field(
        metadata={
            "name": "OrderStatusCheckItemError",
            "type": "Element",
            "required": True,
        }
    )
    order_status_summary_error_info: Optional[
        OrderStatusSummaryErrorInfo
    ] = field(
        default=None,
        metadata={
            "name": "OrderStatusSummaryErrorInfo",
            "type": "Element",
        },
    )
    total_number_of_line_item: Optional[TotalNumberOfLineItem] = field(
        default=None,
        metadata={
            "name": "TotalNumberOfLineItem",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ShipmentStatusEvent:
    status_event: StatusEvent = field(
        metadata={
            "name": "StatusEvent",
            "type": "Element",
            "required": True,
        }
    )
    list_of_status_reason: Optional[ListOfStatusReason] = field(
        default=None,
        metadata={
            "name": "ListOfStatusReason",
            "type": "Element",
        },
    )
    status_note: Optional[StatusNote] = field(
        default=None,
        metadata={
            "name": "StatusNote",
            "type": "Element",
        },
    )
    error_info: Optional[ErrorInfo] = field(
        default=None,
        metadata={
            "name": "ErrorInfo",
            "type": "Element",
        },
    )
    ship_date: Optional[ShipDate] = field(
        default=None,
        metadata={
            "name": "ShipDate",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Status:
    status_event: StatusEvent = field(
        metadata={
            "name": "StatusEvent",
            "type": "Element",
            "required": True,
        }
    )
    list_of_status_reason: Optional[ListOfStatusReason] = field(
        default=None,
        metadata={
            "name": "ListOfStatusReason",
            "type": "Element",
        },
    )
    status_note: Optional[StatusNote] = field(
        default=None,
        metadata={
            "name": "StatusNote",
            "type": "Element",
        },
    )
    error_info: Optional[ErrorInfo] = field(
        default=None,
        metadata={
            "name": "ErrorInfo",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ItemStatusEvent:
    status: Status = field(
        metadata={
            "name": "Status",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderStatus:
    status: Status = field(
        metadata={
            "name": "Status",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PaymentStatusEvent:
    status: Status = field(
        metadata={
            "name": "Status",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ItemStatus:
    item_status_quantity: ItemStatusQuantity = field(
        metadata={
            "name": "ItemStatusQuantity",
            "type": "Element",
            "required": True,
        }
    )
    item_status_event: ItemStatusEvent = field(
        metadata={
            "name": "ItemStatusEvent",
            "type": "Element",
            "required": True,
        }
    )
    payment_status_event: Optional[PaymentStatusEvent] = field(
        default=None,
        metadata={
            "name": "PaymentStatusEvent",
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


@dataclass(kw_only=True)
class OrderStatusResultItem:
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
    order_status_item_result_transport: Optional[
        OrderStatusItemResultTransport
    ] = field(
        default=None,
        metadata={
            "name": "OrderStatusItemResultTransport",
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
    item_status: List[ItemStatus] = field(
        default_factory=list,
        metadata={
            "name": "ItemStatus",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ListOfOrderStatusResultItem:
    order_status_result_item: List[OrderStatusResultItem] = field(
        default_factory=list,
        metadata={
            "name": "OrderStatusResultItem",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class OrderStatusResultReference:
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
    order_status_date: OrderStatusDate = field(
        metadata={
            "name": "OrderStatusDate",
            "type": "Element",
            "required": True,
        }
    )
    order_status: OrderStatus = field(
        metadata={
            "name": "OrderStatus",
            "type": "Element",
            "required": True,
        }
    )
    payment_status_event: Optional[PaymentStatusEvent] = field(
        default=None,
        metadata={
            "name": "PaymentStatusEvent",
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
    list_of_order_status_result_item: Optional[
        ListOfOrderStatusResultItem
    ] = field(
        default=None,
        metadata={
            "name": "ListOfOrderStatusResultItem",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class OrderStatusDetailResult:
    order_status_result_reference: OrderStatusResultReference = field(
        metadata={
            "name": "OrderStatusResultReference",
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
class ListOfOrderStatusResultDetail:
    order_status_detail_result: List[OrderStatusDetailResult] = field(
        default_factory=list,
        metadata={
            "name": "OrderStatusDetailResult",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class OrderStatusResultDetail:
    list_of_order_status_result_detail: ListOfOrderStatusResultDetail = field(
        metadata={
            "name": "ListOfOrderStatusResultDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderStatusResult:
    order_status_result_header: OrderStatusResultHeader = field(
        metadata={
            "name": "OrderStatusResultHeader",
            "type": "Element",
            "required": True,
        }
    )
    order_status_result_detail: Optional[OrderStatusResultDetail] = field(
        default=None,
        metadata={
            "name": "OrderStatusResultDetail",
            "type": "Element",
        },
    )
    order_status_result_summary: Optional[OrderStatusResultSummary] = field(
        default=None,
        metadata={
            "name": "OrderStatusResultSummary",
            "type": "Element",
        },
    )
