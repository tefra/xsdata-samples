from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_result_response import AuctionCreateReference
from xcbl.models.sourcing_result import (
    BaseItemDetail,
    DeliveryDetail,
    InitiatingParty,
    LineItemAttachments,
    ListOfAttachment,
    ListOfNameValueSet,
    ListOfReferenceCoded,
    ListOfStructuredNote,
    OrderDates,
    OrderParty,
    PricingDetail,
    RoundTripInformation,
)
from xcbl.models.sourcing_result_response import Purpose
from xcbl.models.time_series_response import (
    MaximumValue,
    MinimumValue,
)
from xcbl.models.trading_partner_organization_information import Currency
from xcbl.models.trading_partner_response import Reference
from xcbl.models.trading_partner_user_information import Language


@dataclass(kw_only=True)
class AuctionResultSummary:
    total_num_auction_results: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalNumAuctionResults",
            "type": "Element",
        },
    )
    total_num_winning_bids: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalNumWinningBids",
            "type": "Element",
        },
    )
    total_num_participants: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalNumParticipants",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class AuctionResultCurrency:
    currency: Currency = field(
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AuctionResultDates:
    order_dates: OrderDates = field(
        metadata={
            "name": "OrderDates",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AuctionResultId:
    class Meta:
        name = "AuctionResultID"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AuctionResultItemId:
    class Meta:
        name = "AuctionResultItemID"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AuctionResultListOfAttachment:
    list_of_attachment: ListOfAttachment = field(
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AuctionResultParty:
    order_party: OrderParty = field(
        metadata={
            "name": "OrderParty",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AuctionResultPurpose:
    purpose: Purpose = field(
        metadata={
            "name": "Purpose",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfAuctionResultDetailAttachment:
    list_of_attachment: ListOfAttachment = field(
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Range:
    minimum_value: MinimumValue = field(
        metadata={
            "name": "MinimumValue",
            "type": "Element",
            "required": True,
        }
    )
    maximum_value: MaximumValue = field(
        metadata={
            "name": "MaximumValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AuctionResultHeader:
    auction_result_purpose: AuctionResultPurpose = field(
        metadata={
            "name": "AuctionResultPurpose",
            "type": "Element",
            "required": True,
        }
    )
    auction_result_issue_date: str = field(
        metadata={
            "name": "AuctionResultIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    auction_result_id: AuctionResultId = field(
        metadata={
            "name": "AuctionResultID",
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
    forward_auction_indicator: str = field(
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
        },
    )
    language: Language = field(
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
        },
    )
    auction_result_list_of_attachment: Optional[
        AuctionResultListOfAttachment
    ] = field(
        default=None,
        metadata={
            "name": "AuctionResultListOfAttachment",
            "type": "Element",
        },
    )
    auction_result_general_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionResultGeneralNote",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Mvbrange:
    class Meta:
        name = "MVBRange"

    range: Range = field(
        metadata={
            "name": "Range",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Mvbvariable:
    class Meta:
        name = "MVBVariable"

    mvbvariable_name: str = field(
        metadata={
            "name": "MVBVariableName",
            "type": "Element",
            "required": True,
        }
    )
    mvbvariable_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "MVBVariableValue",
            "type": "Element",
        },
    )
    mvbrange: Optional[Mvbrange] = field(
        default=None,
        metadata={
            "name": "MVBRange",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfMvbvariables:
    class Meta:
        name = "ListOfMVBVariables"

    mvbvariable: List[Mvbvariable] = field(
        default_factory=list,
        metadata={
            "name": "MVBVariable",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class AuctionResultItem:
    base_item_detail: BaseItemDetail = field(
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
        },
    )
    delivery_detail: Optional[DeliveryDetail] = field(
        default=None,
        metadata={
            "name": "DeliveryDetail",
            "type": "Element",
        },
    )
    round_trip_information: Optional[RoundTripInformation] = field(
        default=None,
        metadata={
            "name": "RoundTripInformation",
            "type": "Element",
        },
    )
    line_item_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineItemNote",
            "type": "Element",
        },
    )
    list_of_structured_note: Optional[ListOfStructuredNote] = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        },
    )
    list_of_name_value_set: Optional[ListOfNameValueSet] = field(
        default=None,
        metadata={
            "name": "ListOfNameValueSet",
            "type": "Element",
        },
    )
    line_item_attachments: Optional[LineItemAttachments] = field(
        default=None,
        metadata={
            "name": "LineItemAttachments",
            "type": "Element",
        },
    )
    list_of_mvbvariables: Optional[ListOfMvbvariables] = field(
        default=None,
        metadata={
            "name": "ListOfMVBVariables",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfAuctionResultItem:
    auction_result_item: List[AuctionResultItem] = field(
        default_factory=list,
        metadata={
            "name": "AuctionResultItem",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class AuctionResultDetail:
    auction_result_item_id: AuctionResultItemId = field(
        metadata={
            "name": "AuctionResultItemID",
            "type": "Element",
            "required": True,
        }
    )
    winning_bid_indicator: str = field(
        metadata={
            "name": "WinningBidIndicator",
            "type": "Element",
            "required": True,
        }
    )
    auction_result_party: AuctionResultParty = field(
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
        },
    )
    auction_result_currency: Optional[AuctionResultCurrency] = field(
        default=None,
        metadata={
            "name": "AuctionResultCurrency",
            "type": "Element",
        },
    )
    list_of_auction_result_item: ListOfAuctionResultItem = field(
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
        },
    )
    list_of_auction_result_detail_attachment: Optional[
        ListOfAuctionResultDetailAttachment
    ] = field(
        default=None,
        metadata={
            "name": "ListOfAuctionResultDetailAttachment",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfAuctionResultDetail:
    auction_result_detail: List[AuctionResultDetail] = field(
        default_factory=list,
        metadata={
            "name": "AuctionResultDetail",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class AuctionResult:
    auction_result_header: AuctionResultHeader = field(
        metadata={
            "name": "AuctionResultHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_auction_result_detail: ListOfAuctionResultDetail = field(
        metadata={
            "name": "ListOfAuctionResultDetail",
            "type": "Element",
            "required": True,
        }
    )
    auction_result_summary: AuctionResultSummary = field(
        metadata={
            "name": "AuctionResultSummary",
            "type": "Element",
            "required": True,
        }
    )
