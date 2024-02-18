from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create_response import (
    AuctionCreateHeader,
    AuctionCreateSummary,
    AuctionDeliveryDetail,
    AuctionItem,
    AuctionItemDates,
    AuctionPricingDetail,
    ComponentAuctionIndicator,
)
from xcbl.models.auction_result import ListOfMvbvariables
from xcbl.models.sourcing_result import ListOfAttachment


@dataclass(kw_only=True)
class AuctionItemComponent:
    auction_create_detail: "AuctionCreateDetail" = field(
        metadata={
            "name": "AuctionCreateDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfAuctionItemComponents:
    auction_item_component: List[AuctionItemComponent] = field(
        default_factory=list,
        metadata={
            "name": "AuctionItemComponent",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class AuctionCreateDetail:
    auction_item: AuctionItem = field(
        metadata={
            "name": "AuctionItem",
            "type": "Element",
            "required": True,
        }
    )
    list_of_mvbvariables: Optional[ListOfMvbvariables] = field(
        default=None,
        metadata={
            "name": "ListOfMVBVariables",
            "type": "Element",
        },
    )
    auction_pricing_detail: Optional[AuctionPricingDetail] = field(
        default=None,
        metadata={
            "name": "AuctionPricingDetail",
            "type": "Element",
        },
    )
    auction_item_dates: Optional[AuctionItemDates] = field(
        default=None,
        metadata={
            "name": "AuctionItemDates",
            "type": "Element",
        },
    )
    auction_delivery_detail: Optional[AuctionDeliveryDetail] = field(
        default=None,
        metadata={
            "name": "AuctionDeliveryDetail",
            "type": "Element",
        },
    )
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
        },
    )
    component_auction_indicator: ComponentAuctionIndicator = field(
        metadata={
            "name": "ComponentAuctionIndicator",
            "type": "Element",
            "required": True,
        }
    )
    list_of_auction_item_components: Optional[
        ListOfAuctionItemComponents
    ] = field(
        default=None,
        metadata={
            "name": "ListOfAuctionItemComponents",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfAuctionCreateDetail:
    auction_create_detail: List[AuctionCreateDetail] = field(
        default_factory=list,
        metadata={
            "name": "AuctionCreateDetail",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class AuctionCreate:
    auction_create_header: AuctionCreateHeader = field(
        metadata={
            "name": "AuctionCreateHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_auction_create_detail: ListOfAuctionCreateDetail = field(
        metadata={
            "name": "ListOfAuctionCreateDetail",
            "type": "Element",
            "required": True,
        }
    )
    auction_create_summary: AuctionCreateSummary = field(
        metadata={
            "name": "AuctionCreateSummary",
            "type": "Element",
            "required": True,
        }
    )
