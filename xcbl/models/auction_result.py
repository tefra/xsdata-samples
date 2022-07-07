from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    Currency,
    DeliveryDetail,
    InitiatingParty,
    Language,
    ListOfAttachment,
    ListOfMvbvariables,
    ListOfReferenceCoded,
    OrderDates,
    Purpose,
    Reference,
)
from xcbl.models.order_request import (
    BaseItemDetail,
    LineItemAttachments,
    ListOfNameValueSet,
    ListOfStructuredNote,
    PricingDetail,
    RoundTripInformation,
)
from xcbl.models.request_for_quotation import OrderParty


@dataclass
class AuctionResultSummary:
    total_num_auction_results: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalNumAuctionResults",
            "type": "Element",
        }
    )
    total_num_winning_bids: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalNumWinningBids",
            "type": "Element",
        }
    )
    total_num_participants: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalNumParticipants",
            "type": "Element",
        }
    )


@dataclass
class AuctionCreateReference:
    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AuctionResultCurrency:
    currency: Optional[Currency] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AuctionResultDates:
    order_dates: Optional[OrderDates] = field(
        default=None,
        metadata={
            "name": "OrderDates",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AuctionResultId:
    class Meta:
        name = "AuctionResultID"

    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AuctionResultItem:
    base_item_detail: Optional[BaseItemDetail] = field(
        default=None,
        metadata={
            "name": "BaseItemDetail",
            "type": "Element",
            "required": True,
        }
    )
    pricing_detail: Optional[PricingDetail] = field(
        default=None,
        metadata={
            "name": "PricingDetail",
            "type": "Element",
        }
    )
    delivery_detail: Optional[DeliveryDetail] = field(
        default=None,
        metadata={
            "name": "DeliveryDetail",
            "type": "Element",
        }
    )
    round_trip_information: Optional[RoundTripInformation] = field(
        default=None,
        metadata={
            "name": "RoundTripInformation",
            "type": "Element",
        }
    )
    line_item_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineItemNote",
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
    line_item_attachments: Optional[LineItemAttachments] = field(
        default=None,
        metadata={
            "name": "LineItemAttachments",
            "type": "Element",
        }
    )
    list_of_mvbvariables: Optional[ListOfMvbvariables] = field(
        default=None,
        metadata={
            "name": "ListOfMVBVariables",
            "type": "Element",
        }
    )


@dataclass
class AuctionResultItemId:
    class Meta:
        name = "AuctionResultItemID"

    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AuctionResultListOfAttachment:
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AuctionResultParty:
    order_party: Optional[OrderParty] = field(
        default=None,
        metadata={
            "name": "OrderParty",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AuctionResultPurpose:
    purpose: Optional[Purpose] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfAuctionResultDetailAttachment:
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AuctionResultHeader:
    auction_result_purpose: Optional[AuctionResultPurpose] = field(
        default=None,
        metadata={
            "name": "AuctionResultPurpose",
            "type": "Element",
            "required": True,
        }
    )
    auction_result_issue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionResultIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    auction_result_id: Optional[AuctionResultId] = field(
        default=None,
        metadata={
            "name": "AuctionResultID",
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
    forward_auction_indicator: Optional[str] = field(
        default=None,
        metadata={
            "name": "ForwardAuctionIndicator",
            "type": "Element",
            "required": True,
        }
    )
    initiating_party: Optional[InitiatingParty] = field(
        default=None,
        metadata={
            "name": "InitiatingParty",
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
    list_of_reference_coded: Optional[ListOfReferenceCoded] = field(
        default=None,
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
        }
    )
    auction_result_list_of_attachment: Optional[AuctionResultListOfAttachment] = field(
        default=None,
        metadata={
            "name": "AuctionResultListOfAttachment",
            "type": "Element",
        }
    )
    auction_result_general_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionResultGeneralNote",
            "type": "Element",
        }
    )


@dataclass
class ListOfAuctionResultItem:
    auction_result_item: List[AuctionResultItem] = field(
        default_factory=list,
        metadata={
            "name": "AuctionResultItem",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class AuctionResultDetail:
    auction_result_item_id: Optional[AuctionResultItemId] = field(
        default=None,
        metadata={
            "name": "AuctionResultItemID",
            "type": "Element",
            "required": True,
        }
    )
    winning_bid_indicator: Optional[str] = field(
        default=None,
        metadata={
            "name": "WinningBidIndicator",
            "type": "Element",
            "required": True,
        }
    )
    auction_result_party: Optional[AuctionResultParty] = field(
        default=None,
        metadata={
            "name": "AuctionResultParty",
            "type": "Element",
            "required": True,
        }
    )
    auction_result_dates: Optional[AuctionResultDates] = field(
        default=None,
        metadata={
            "name": "AuctionResultDates",
            "type": "Element",
        }
    )
    auction_result_currency: Optional[AuctionResultCurrency] = field(
        default=None,
        metadata={
            "name": "AuctionResultCurrency",
            "type": "Element",
        }
    )
    list_of_auction_result_item: Optional[ListOfAuctionResultItem] = field(
        default=None,
        metadata={
            "name": "ListOfAuctionResultItem",
            "type": "Element",
            "required": True,
        }
    )
    auction_result_detail_notes: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionResultDetailNotes",
            "type": "Element",
        }
    )
    list_of_auction_result_detail_attachment: Optional[ListOfAuctionResultDetailAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAuctionResultDetailAttachment",
            "type": "Element",
        }
    )


@dataclass
class ListOfAuctionResultDetail:
    auction_result_detail: List[AuctionResultDetail] = field(
        default_factory=list,
        metadata={
            "name": "AuctionResultDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class AuctionResult:
    auction_result_header: Optional[AuctionResultHeader] = field(
        default=None,
        metadata={
            "name": "AuctionResultHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_auction_result_detail: Optional[ListOfAuctionResultDetail] = field(
        default=None,
        metadata={
            "name": "ListOfAuctionResultDetail",
            "type": "Element",
            "required": True,
        }
    )
    auction_result_summary: Optional[AuctionResultSummary] = field(
        default=None,
        metadata={
            "name": "AuctionResultSummary",
            "type": "Element",
            "required": True,
        }
    )
