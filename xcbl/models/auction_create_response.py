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


@dataclass
class AuctionItemComponentResponse:
    auction_create_response_detail: Optional["AuctionCreateResponseDetail"] = field(
        default=None,
        metadata={
            "name": "AuctionCreateResponseDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AuctionCreateResponsePurpose:
    purpose: Optional[Purpose] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AuctionCreateResponseSummary:
    auction_create_summary: Optional[AuctionCreateSummary] = field(
        default=None,
        metadata={
            "name": "AuctionCreateSummary",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ChangedAuctionCreateDetail:
    auction_detail: Optional[AuctionDetail] = field(
        default=None,
        metadata={
            "name": "AuctionDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ChangedAuctionCreateHeader:
    auction_create_header: Optional[AuctionCreateHeader] = field(
        default=None,
        metadata={
            "name": "AuctionCreateHeader",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfAuctionItemComponentResponse:
    auction_item_component_response: List[AuctionItemComponentResponse] = field(
        default_factory=list,
        metadata={
            "name": "AuctionItemComponentResponse",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class AuctionCreateResponseDetail:
    auction_item_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionItemID",
            "type": "Element",
            "required": True,
        }
    )
    auction_item_name: Optional[str] = field(
        default=None,
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
    auction_item_hierarchy_level: Optional[str] = field(
        default=None,
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
    auction_item_response_coded: Optional[str] = field(
        default=None,
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


@dataclass
class AuctionCreateResponseHeader:
    auction_create_response_purpose: Optional[AuctionCreateResponsePurpose] = field(
        default=None,
        metadata={
            "name": "AuctionCreateResponsePurpose",
            "type": "Element",
            "required": True,
        }
    )
    auction_create_response_issue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionCreateResponseIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    auction_create_response_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionCreateResponseID",
            "type": "Element",
            "required": True,
        }
    )
    auction_create_reference: Optional[AuctionCreateReference] = field(
        default=None,
        metadata={
            "name": "AuctionCreateReference",
            "type": "Element",
            "required": True,
        }
    )
    auction_response_coded: Optional[str] = field(
        default=None,
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
    language: Optional[Language] = field(
        default=None,
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


@dataclass
class ListOfAuctionCreateResponseDetail:
    auction_create_response_detail: List[AuctionCreateResponseDetail] = field(
        default_factory=list,
        metadata={
            "name": "AuctionCreateResponseDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class AuctionCreateResponse:
    auction_create_response_header: Optional[AuctionCreateResponseHeader] = field(
        default=None,
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
    auction_create_response_summary: Optional[AuctionCreateResponseSummary] = field(
        default=None,
        metadata={
            "name": "AuctionCreateResponseSummary",
            "type": "Element",
            "required": True,
        }
    )
