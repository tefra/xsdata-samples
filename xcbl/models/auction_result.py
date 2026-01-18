from __future__ import annotations

from dataclasses import dataclass, field

from xcbl.models.auction_result_response import AuctionCreateReference
from xcbl.models.sourcing_result import (
    BaseItemDetail,
    DeliveryDetail,
    InitiatingParty,
    LineItemAttachments,
    LineItemNote,
    ListOfAttachment,
    ListOfNameValueSet,
    ListOfReferenceCoded,
    ListOfStructuredNote,
    OrderDates,
    OrderParty,
    PricingDetail,
    RoundTripInformation,
    TotalNumParticipants,
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
class AuctionResultDetailNotes:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AuctionResultGeneralNote:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AuctionResultIssueDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ForwardAuctionIndicator:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class MvbvariableName:
    class Meta:
        name = "MVBVariableName"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class MvbvariableValue:
    class Meta:
        name = "MVBVariableValue"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TotalNumAuctionResults:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TotalNumWinningBids:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class WinningBidIndicator:
    value: str = field(
        default="",
        metadata={
            "required": True,
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
class AuctionResultSummary:
    total_num_auction_results: TotalNumAuctionResults | None = field(
        default=None,
        metadata={
            "name": "TotalNumAuctionResults",
            "type": "Element",
        },
    )
    total_num_winning_bids: TotalNumWinningBids | None = field(
        default=None,
        metadata={
            "name": "TotalNumWinningBids",
            "type": "Element",
        },
    )
    total_num_participants: TotalNumParticipants | None = field(
        default=None,
        metadata={
            "name": "TotalNumParticipants",
            "type": "Element",
        },
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
    auction_result_issue_date: AuctionResultIssueDate = field(
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
    forward_auction_indicator: ForwardAuctionIndicator = field(
        metadata={
            "name": "ForwardAuctionIndicator",
            "type": "Element",
            "required": True,
        }
    )
    initiating_party: InitiatingParty | None = field(
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
    list_of_reference_coded: ListOfReferenceCoded | None = field(
        default=None,
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
        },
    )
    auction_result_list_of_attachment: AuctionResultListOfAttachment | None = (
        field(
            default=None,
            metadata={
                "name": "AuctionResultListOfAttachment",
                "type": "Element",
            },
        )
    )
    auction_result_general_note: AuctionResultGeneralNote | None = field(
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

    mvbvariable_name: MvbvariableName = field(
        metadata={
            "name": "MVBVariableName",
            "type": "Element",
            "required": True,
        }
    )
    mvbvariable_value: MvbvariableValue | None = field(
        default=None,
        metadata={
            "name": "MVBVariableValue",
            "type": "Element",
        },
    )
    mvbrange: Mvbrange | None = field(
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

    mvbvariable: list[Mvbvariable] = field(
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
    pricing_detail: PricingDetail | None = field(
        default=None,
        metadata={
            "name": "PricingDetail",
            "type": "Element",
        },
    )
    delivery_detail: DeliveryDetail | None = field(
        default=None,
        metadata={
            "name": "DeliveryDetail",
            "type": "Element",
        },
    )
    round_trip_information: RoundTripInformation | None = field(
        default=None,
        metadata={
            "name": "RoundTripInformation",
            "type": "Element",
        },
    )
    line_item_note: LineItemNote | None = field(
        default=None,
        metadata={
            "name": "LineItemNote",
            "type": "Element",
        },
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
    line_item_attachments: LineItemAttachments | None = field(
        default=None,
        metadata={
            "name": "LineItemAttachments",
            "type": "Element",
        },
    )
    list_of_mvbvariables: ListOfMvbvariables | None = field(
        default=None,
        metadata={
            "name": "ListOfMVBVariables",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfAuctionResultItem:
    auction_result_item: list[AuctionResultItem] = field(
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
    winning_bid_indicator: WinningBidIndicator = field(
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
    auction_result_dates: AuctionResultDates | None = field(
        default=None,
        metadata={
            "name": "AuctionResultDates",
            "type": "Element",
        },
    )
    auction_result_currency: AuctionResultCurrency | None = field(
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
    auction_result_detail_notes: AuctionResultDetailNotes | None = field(
        default=None,
        metadata={
            "name": "AuctionResultDetailNotes",
            "type": "Element",
        },
    )
    list_of_auction_result_detail_attachment: (
        ListOfAuctionResultDetailAttachment | None
    ) = field(
        default=None,
        metadata={
            "name": "ListOfAuctionResultDetailAttachment",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfAuctionResultDetail:
    auction_result_detail: list[AuctionResultDetail] = field(
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
