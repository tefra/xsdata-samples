from __future__ import annotations

from dataclasses import dataclass, field

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
    status_event_coded_other: StatusEventCodedOther | None = field(
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
    order_status_result_language: OrderStatusResultLanguage | None = field(
        default=None,
        metadata={
            "name": "OrderStatusResultLanguage",
            "type": "Element",
        },
    )
    order_status_result_note: OrderStatusResultNote | None = field(
        default=None,
        metadata={
            "name": "OrderStatusResultNote",
            "type": "Element",
        },
    )
    result_list_of_attachment: ResultListOfAttachment | None = field(
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
    order_status_summary_error_info: OrderStatusSummaryErrorInfo | None = (
        field(
            default=None,
            metadata={
                "name": "OrderStatusSummaryErrorInfo",
                "type": "Element",
            },
        )
    )
    total_number_of_line_item: TotalNumberOfLineItem | None = field(
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
    list_of_status_reason: ListOfStatusReason | None = field(
        default=None,
        metadata={
            "name": "ListOfStatusReason",
            "type": "Element",
        },
    )
    status_note: StatusNote | None = field(
        default=None,
        metadata={
            "name": "StatusNote",
            "type": "Element",
        },
    )
    error_info: ErrorInfo | None = field(
        default=None,
        metadata={
            "name": "ErrorInfo",
            "type": "Element",
        },
    )
    ship_date: ShipDate | None = field(
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
    list_of_status_reason: ListOfStatusReason | None = field(
        default=None,
        metadata={
            "name": "ListOfStatusReason",
            "type": "Element",
        },
    )
    status_note: StatusNote | None = field(
        default=None,
        metadata={
            "name": "StatusNote",
            "type": "Element",
        },
    )
    error_info: ErrorInfo | None = field(
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
    payment_status_event: PaymentStatusEvent | None = field(
        default=None,
        metadata={
            "name": "PaymentStatusEvent",
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


@dataclass(kw_only=True)
class OrderStatusResultItem:
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
    order_status_item_result_transport: (
        OrderStatusItemResultTransport | None
    ) = field(
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
    item_status: list[ItemStatus] = field(
        default_factory=list,
        metadata={
            "name": "ItemStatus",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ListOfOrderStatusResultItem:
    order_status_result_item: list[OrderStatusResultItem] = field(
        default_factory=list,
        metadata={
            "name": "OrderStatusResultItem",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class OrderStatusResultReference:
    account_code: AccountCode | None = field(
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
    other_reference: OtherReference | None = field(
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
    payment_status_event: PaymentStatusEvent | None = field(
        default=None,
        metadata={
            "name": "PaymentStatusEvent",
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
    list_of_order_status_result_item: ListOfOrderStatusResultItem | None = (
        field(
            default=None,
            metadata={
                "name": "ListOfOrderStatusResultItem",
                "type": "Element",
            },
        )
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
class ListOfOrderStatusResultDetail:
    order_status_detail_result: list[OrderStatusDetailResult] = field(
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
    order_status_result_detail: OrderStatusResultDetail | None = field(
        default=None,
        metadata={
            "name": "OrderStatusResultDetail",
            "type": "Element",
        },
    )
    order_status_result_summary: OrderStatusResultSummary | None = field(
        default=None,
        metadata={
            "name": "OrderStatusResultSummary",
            "type": "Element",
        },
    )
