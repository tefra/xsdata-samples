from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    AuctionCreateHeader,
    AuctionCreateSummary,
    AuctionDetail,
    Language,
    Purpose,
)
from xcbl.models.auction_result import AuctionCreateReference


@dataclass(kw_only=True)
class AuctionItemComponentResponse:
    auction_create_response_detail: "AuctionCreateResponseDetail" = field(
        metadata={
            "name": "AuctionCreateResponseDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AuctionCreateResponsePurpose:
    purpose: Purpose = field(
        metadata={
            "name": "Purpose",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AuctionCreateResponseSummary:
    auction_create_summary: AuctionCreateSummary = field(
        metadata={
            "name": "AuctionCreateSummary",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ChangedAuctionCreateDetail:
    auction_detail: AuctionDetail = field(
        metadata={
            "name": "AuctionDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ChangedAuctionCreateHeader:
    auction_create_header: AuctionCreateHeader = field(
        metadata={
            "name": "AuctionCreateHeader",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfAuctionItemComponentResponse:
    auction_item_component_response: List[AuctionItemComponentResponse] = field(
        default_factory=list,
        metadata={
            "name": "AuctionItemComponentResponse",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class AuctionCreateResponseDetail:
    auction_item_id: str = field(
        metadata={
            "name": "AuctionItemID",
            "type": "Element",
            "required": True,
        }
    )
    auction_item_name: str = field(
        metadata={
            "name": "AuctionItemName",
            "type": "Element",
            "required": True,
        }
    )
    auction_item_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionItemDescription",
            "type": "Element",
        }
    )
    auction_item_hierarchy_level: str = field(
        metadata={
            "name": "AuctionItemHierarchyLevel",
            "type": "Element",
            "required": True,
        }
    )
    auction_line_item_num: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionLineItemNum",
            "type": "Element",
        }
    )
    auction_item_response_coded: str = field(
        metadata={
            "name": "AuctionItemResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    auction_item_response_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionItemResponseCodedOther",
            "type": "Element",
        }
    )
    changed_auction_create_detail: Optional[ChangedAuctionCreateDetail] = field(
        default=None,
        metadata={
            "name": "ChangedAuctionCreateDetail",
            "type": "Element",
        }
    )
    list_of_auction_item_component_response: Optional[ListOfAuctionItemComponentResponse] = field(
        default=None,
        metadata={
            "name": "ListOfAuctionItemComponentResponse",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class AuctionCreateResponseHeader:
    auction_create_response_purpose: AuctionCreateResponsePurpose = field(
        metadata={
            "name": "AuctionCreateResponsePurpose",
            "type": "Element",
            "required": True,
        }
    )
    auction_create_response_issue_date: str = field(
        metadata={
            "name": "AuctionCreateResponseIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    auction_create_response_id: str = field(
        metadata={
            "name": "AuctionCreateResponseID",
            "type": "Element",
            "required": True,
        }
    )
    auction_create_reference: AuctionCreateReference = field(
        metadata={
            "name": "AuctionCreateReference",
            "type": "Element",
            "required": True,
        }
    )
    auction_response_coded: str = field(
        metadata={
            "name": "AuctionResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    auction_response_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionResponseCodedOther",
            "type": "Element",
        }
    )
    changed_auction_create_header: Optional[ChangedAuctionCreateHeader] = field(
        default=None,
        metadata={
            "name": "ChangedAuctionCreateHeader",
            "type": "Element",
        }
    )
    language: Language = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )
    auction_create_response_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionCreateResponseNote",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ListOfAuctionCreateResponseDetail:
    auction_create_response_detail: List[AuctionCreateResponseDetail] = field(
        default_factory=list,
        metadata={
            "name": "AuctionCreateResponseDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class AuctionCreateResponse:
    auction_create_response_header: AuctionCreateResponseHeader = field(
        metadata={
            "name": "AuctionCreateResponseHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_auction_create_response_detail: Optional[ListOfAuctionCreateResponseDetail] = field(
        default=None,
        metadata={
            "name": "ListOfAuctionCreateResponseDetail",
            "type": "Element",
        }
    )
    auction_create_response_summary: AuctionCreateResponseSummary = field(
        metadata={
            "name": "AuctionCreateResponseSummary",
            "type": "Element",
            "required": True,
        }
    )
