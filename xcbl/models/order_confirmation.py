from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    Currency,
    Language,
    ListOfAttachment,
    ListOfReferenceCoded,
)
from xcbl.models.invoice import PurchaseOrderReference
from xcbl.models.order_confirmation_response import (
    ListOfAccountAssignment,
    OrderConfirmationType,
)
from xcbl.models.order_request import (
    BuyerParty,
    CatalogReference,
    Category,
    ContractId,
    ItemDetail,
    ListOfNameValueSet,
    ListOfPartyCoded,
    ListOfStructuredNote,
    SellerParty,
    ShipToParty,
)


@dataclass
class OrderConfirmationAction:
    order_confirmation_action_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderConfirmationActionCoded",
            "type": "Element",
            "required": True,
        }
    )
    order_confirmation_action_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderConfirmationActionCodedOther",
            "type": "Element",
        }
    )


@dataclass
class ContractAndSystemReference:
    contract_id: Optional[ContractId] = field(
        default=None,
        metadata={
            "name": "ContractID",
            "type": "Element",
            "required": True,
        }
    )
    contract_item_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContractItemID",
            "type": "Element",
            "required": True,
        }
    )
    system_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SystemID",
            "type": "Element",
        }
    )


@dataclass
class OrderConfirmationParty:
    buyer_party: Optional[BuyerParty] = field(
        default=None,
        metadata={
            "name": "BuyerParty",
            "type": "Element",
        }
    )
    seller_party: Optional[SellerParty] = field(
        default=None,
        metadata={
            "name": "SellerParty",
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
    list_of_party_coded: Optional[ListOfPartyCoded] = field(
        default=None,
        metadata={
            "name": "ListOfPartyCoded",
            "type": "Element",
        }
    )


@dataclass
class OrderConfirmationDetailReferences:
    purchase_order_reference: Optional[PurchaseOrderReference] = field(
        default=None,
        metadata={
            "name": "PurchaseOrderReference",
            "type": "Element",
            "required": True,
        }
    )
    category: Optional[Category] = field(
        default=None,
        metadata={
            "name": "Category",
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
    contract_and_system_reference: Optional[ContractAndSystemReference] = field(
        default=None,
        metadata={
            "name": "ContractAndSystemReference",
            "type": "Element",
        }
    )
    list_of_reference_coded: Optional[ListOfReferenceCoded] = field(
        default=None,
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
        }
    )


@dataclass
class OrderConfirmationHeader:
    seller_order_confirmation_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SellerOrderConfirmationNumber",
            "type": "Element",
            "required": True,
        }
    )
    seller_order_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SellerOrderNumber",
            "type": "Element",
            "required": True,
        }
    )
    order_confirmation_issue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderConfirmationIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    order_confirmation_type: Optional[OrderConfirmationType] = field(
        default=None,
        metadata={
            "name": "OrderConfirmationType",
            "type": "Element",
        }
    )
    language: Optional[Language] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
        }
    )
    currency: Optional[Currency] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
        }
    )
    order_confirmation_party: Optional[OrderConfirmationParty] = field(
        default=None,
        metadata={
            "name": "OrderConfirmationParty",
            "type": "Element",
        }
    )
    order_confirmation_action: Optional[OrderConfirmationAction] = field(
        default=None,
        metadata={
            "name": "OrderConfirmationAction",
            "type": "Element",
        }
    )
    order_confirmation_header_short_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderConfirmationHeaderShortDescription",
            "type": "Element",
        }
    )
    order_confirmation_header_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderConfirmationHeaderNote",
            "type": "Element",
        }
    )
    list_of_structured_note: Optional[ListOfStructuredNote] = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        }
    )
    list_of_name_value_set: Optional[ListOfNameValueSet] = field(
        default=None,
        metadata={
            "name": "ListOfNameValueSet",
            "type": "Element",
        }
    )
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
        }
    )


@dataclass
class OrderConfirmationItemDetail:
    order_confirmation_item_num: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderConfirmationItemNum",
            "type": "Element",
            "required": True,
        }
    )
    order_confirmation_action: Optional[OrderConfirmationAction] = field(
        default=None,
        metadata={
            "name": "OrderConfirmationAction",
            "type": "Element",
        }
    )
    order_confirmation_detail_short_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderConfirmationDetailShortDescription",
            "type": "Element",
        }
    )
    order_confirmation_detail_references: Optional[OrderConfirmationDetailReferences] = field(
        default=None,
        metadata={
            "name": "OrderConfirmationDetailReferences",
            "type": "Element",
            "required": True,
        }
    )
    delivery_complete: Optional[str] = field(
        default=None,
        metadata={
            "name": "DeliveryComplete",
            "type": "Element",
        }
    )
    item_detail: Optional[ItemDetail] = field(
        default=None,
        metadata={
            "name": "ItemDetail",
            "type": "Element",
            "required": True,
        }
    )
    list_of_account_assignment: Optional[ListOfAccountAssignment] = field(
        default=None,
        metadata={
            "name": "ListOfAccountAssignment",
            "type": "Element",
        }
    )


@dataclass
class ListOfOrderConfirmationItemDetail:
    order_confirmation_item_detail: List[OrderConfirmationItemDetail] = field(
        default_factory=list,
        metadata={
            "name": "OrderConfirmationItemDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class OrderConfirmationDetail:
    list_of_order_confirmation_item_detail: Optional[ListOfOrderConfirmationItemDetail] = field(
        default=None,
        metadata={
            "name": "ListOfOrderConfirmationItemDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OrderConfirmation:
    order_confirmation_header: Optional[OrderConfirmationHeader] = field(
        default=None,
        metadata={
            "name": "OrderConfirmationHeader",
            "type": "Element",
            "required": True,
        }
    )
    order_confirmation_detail: Optional[OrderConfirmationDetail] = field(
        default=None,
        metadata={
            "name": "OrderConfirmationDetail",
            "type": "Element",
            "required": True,
        }
    )
