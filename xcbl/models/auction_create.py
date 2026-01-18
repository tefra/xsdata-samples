from __future__ import annotations

from dataclasses import dataclass, field

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
class AuctionCreateDetail:
    auction_item: AuctionItem = field(
        metadata={
            "name": "AuctionItem",
            "type": "Element",
            "required": True,
        }
    )
    list_of_mvbvariables: ListOfMvbvariables | None = field(
        default=None,
        metadata={
            "name": "ListOfMVBVariables",
            "type": "Element",
        },
    )
    auction_pricing_detail: AuctionPricingDetail | None = field(
        default=None,
        metadata={
            "name": "AuctionPricingDetail",
            "type": "Element",
        },
    )
    auction_item_dates: AuctionItemDates | None = field(
        default=None,
        metadata={
            "name": "AuctionItemDates",
            "type": "Element",
        },
    )
    auction_delivery_detail: AuctionDeliveryDetail | None = field(
        default=None,
        metadata={
            "name": "AuctionDeliveryDetail",
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
    component_auction_indicator: ComponentAuctionIndicator = field(
        metadata={
            "name": "ComponentAuctionIndicator",
            "type": "Element",
            "required": True,
        }
    )
    list_of_auction_item_components: ListOfAuctionItemComponents | None = (
        field(
            default=None,
            metadata={
                "name": "ListOfAuctionItemComponents",
                "type": "Element",
            },
        )
    )


@dataclass(kw_only=True)
class AuctionItemComponent:
    auction_create_detail: AuctionCreateDetail = field(
        metadata={
            "name": "AuctionCreateDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfAuctionCreateDetail:
    auction_create_detail: list[AuctionCreateDetail] = field(
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


@dataclass(kw_only=True)
class ListOfAuctionItemComponents:
    auction_item_component: list[AuctionItemComponent] = field(
        default_factory=list,
        metadata={
            "name": "AuctionItemComponent",
            "type": "Element",
            "min_occurs": 1,
        },
    )
