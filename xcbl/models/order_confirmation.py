from dataclasses import dataclass, field
from typing import Optional

from xcbl.models.order_confirmation_response import (
    ListOfAccountAssignment,
    OrderConfirmationItemNum,
    OrderConfirmationType,
)
from xcbl.models.remittance_advice import PurchaseOrderReference
from xcbl.models.shipping_schedule_response import SellerOrderNumber
from xcbl.models.sourcing_result import (
    BuyerParty,
    CatalogReference,
    Category,
    ContractId,
    ItemDetail,
    ListOfAttachment,
    ListOfNameValueSet,
    ListOfReferenceCoded,
    ListOfStructuredNote,
    SellerParty,
    ShipToParty,
    SystemId,
)
from xcbl.models.time_series_response import ListOfPartyCoded
from xcbl.models.trading_partner_organization_information import Currency
from xcbl.models.trading_partner_user_information import Language


@dataclass(kw_only=True)
class ContractItemId:
    class Meta:
        name = "ContractItemID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class DeliveryComplete:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class OrderConfirmationActionCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class OrderConfirmationActionCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class OrderConfirmationDetailShortDescription:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class OrderConfirmationHeaderNote:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class OrderConfirmationHeaderShortDescription:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class OrderConfirmationIssueDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SellerOrderConfirmationNumber:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ContractAndSystemReference:
    contract_id: ContractId = field(
        metadata={
            "name": "ContractID",
            "type": "Element",
            "required": True,
        }
    )
    contract_item_id: ContractItemId = field(
        metadata={
            "name": "ContractItemID",
            "type": "Element",
            "required": True,
        }
    )
    system_id: SystemId | None = field(
        default=None,
        metadata={
            "name": "SystemID",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class OrderConfirmationAction:
    order_confirmation_action_coded: OrderConfirmationActionCoded = field(
        metadata={
            "name": "OrderConfirmationActionCoded",
            "type": "Element",
            "required": True,
        }
    )
    order_confirmation_action_coded_other: OrderConfirmationActionCodedOther | None = field(
        default=None,
        metadata={
            "name": "OrderConfirmationActionCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class OrderConfirmationParty:
    buyer_party: BuyerParty | None = field(
        default=None,
        metadata={
            "name": "BuyerParty",
            "type": "Element",
        },
    )
    seller_party: SellerParty | None = field(
        default=None,
        metadata={
            "name": "SellerParty",
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
    list_of_party_coded: ListOfPartyCoded | None = field(
        default=None,
        metadata={
            "name": "ListOfPartyCoded",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class OrderConfirmationDetailReferences:
    purchase_order_reference: PurchaseOrderReference = field(
        metadata={
            "name": "PurchaseOrderReference",
            "type": "Element",
            "required": True,
        }
    )
    category: Category | None = field(
        default=None,
        metadata={
            "name": "Category",
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
    contract_and_system_reference: ContractAndSystemReference | None = (
        field(
            default=None,
            metadata={
                "name": "ContractAndSystemReference",
                "type": "Element",
            },
        )
    )
    list_of_reference_coded: ListOfReferenceCoded | None = field(
        default=None,
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class OrderConfirmationHeader:
    seller_order_confirmation_number: SellerOrderConfirmationNumber = field(
        metadata={
            "name": "SellerOrderConfirmationNumber",
            "type": "Element",
            "required": True,
        }
    )
    seller_order_number: SellerOrderNumber = field(
        metadata={
            "name": "SellerOrderNumber",
            "type": "Element",
            "required": True,
        }
    )
    order_confirmation_issue_date: OrderConfirmationIssueDate = field(
        metadata={
            "name": "OrderConfirmationIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    order_confirmation_type: OrderConfirmationType | None = field(
        default=None,
        metadata={
            "name": "OrderConfirmationType",
            "type": "Element",
        },
    )
    language: Language | None = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
        },
    )
    currency: Currency | None = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
        },
    )
    order_confirmation_party: OrderConfirmationParty | None = field(
        default=None,
        metadata={
            "name": "OrderConfirmationParty",
            "type": "Element",
        },
    )
    order_confirmation_action: OrderConfirmationAction | None = field(
        default=None,
        metadata={
            "name": "OrderConfirmationAction",
            "type": "Element",
        },
    )
    order_confirmation_header_short_description: OrderConfirmationHeaderShortDescription | None = field(
        default=None,
        metadata={
            "name": "OrderConfirmationHeaderShortDescription",
            "type": "Element",
        },
    )
    order_confirmation_header_note: OrderConfirmationHeaderNote | None = (
        field(
            default=None,
            metadata={
                "name": "OrderConfirmationHeaderNote",
                "type": "Element",
            },
        )
    )
    list_of_structured_note: ListOfStructuredNote | None = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        },
    )
    list_of_name_value_set: ListOfNameValueSet | None = field(
        default=None,
        metadata={
            "name": "ListOfNameValueSet",
            "type": "Element",
        },
    )
    list_of_attachment: ListOfAttachment | None = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class OrderConfirmationItemDetail:
    order_confirmation_item_num: OrderConfirmationItemNum = field(
        metadata={
            "name": "OrderConfirmationItemNum",
            "type": "Element",
            "required": True,
        }
    )
    order_confirmation_action: OrderConfirmationAction | None = field(
        default=None,
        metadata={
            "name": "OrderConfirmationAction",
            "type": "Element",
        },
    )
    order_confirmation_detail_short_description: OrderConfirmationDetailShortDescription | None = field(
        default=None,
        metadata={
            "name": "OrderConfirmationDetailShortDescription",
            "type": "Element",
        },
    )
    order_confirmation_detail_references: OrderConfirmationDetailReferences = (
        field(
            metadata={
                "name": "OrderConfirmationDetailReferences",
                "type": "Element",
                "required": True,
            }
        )
    )
    delivery_complete: DeliveryComplete | None = field(
        default=None,
        metadata={
            "name": "DeliveryComplete",
            "type": "Element",
        },
    )
    item_detail: ItemDetail = field(
        metadata={
            "name": "ItemDetail",
            "type": "Element",
            "required": True,
        }
    )
    list_of_account_assignment: ListOfAccountAssignment | None = field(
        default=None,
        metadata={
            "name": "ListOfAccountAssignment",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfOrderConfirmationItemDetail:
    order_confirmation_item_detail: list[OrderConfirmationItemDetail] = field(
        default_factory=list,
        metadata={
            "name": "OrderConfirmationItemDetail",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class OrderConfirmationDetail:
    list_of_order_confirmation_item_detail: ListOfOrderConfirmationItemDetail = field(
        metadata={
            "name": "ListOfOrderConfirmationItemDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderConfirmation:
    order_confirmation_header: OrderConfirmationHeader = field(
        metadata={
            "name": "OrderConfirmationHeader",
            "type": "Element",
            "required": True,
        }
    )
    order_confirmation_detail: OrderConfirmationDetail = field(
        metadata={
            "name": "OrderConfirmationDetail",
            "type": "Element",
            "required": True,
        }
    )
