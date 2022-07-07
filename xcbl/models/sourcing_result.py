from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    Currency,
    InitiatingParty,
    Language,
    ListOfAttachment,
    ListOfReferenceCoded,
    OrderDates,
    Purpose,
    Reference,
)
from xcbl.models.order_request import ItemDetail
from xcbl.models.request_for_quotation import OrderParty
from xcbl.models.sourcing_create_response import SourcingCreateReference


@dataclass
class QuoteAwardDetails:
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        }
    )
    number_of_line_items_awarded: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumberOfLineItemsAwarded",
            "type": "Element",
            "required": True,
        }
    )
    total_award_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalAwardValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfSourcingResultDetailAttachment:
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SourcingResultCurrency:
    currency: Optional[Currency] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SourcingResultDates:
    order_dates: Optional[OrderDates] = field(
        default=None,
        metadata={
            "name": "OrderDates",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SourcingResultId:
    class Meta:
        name = "SourcingResultID"

    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SourcingResultItem:
    item_detail: Optional[ItemDetail] = field(
        default=None,
        metadata={
            "name": "ItemDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SourcingResultItemId:
    class Meta:
        name = "SourcingResultItemID"

    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SourcingResultListOfAttachment:
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SourcingResultParty:
    order_party: Optional[OrderParty] = field(
        default=None,
        metadata={
            "name": "OrderParty",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SourcingResultPurpose:
    purpose: Optional[Purpose] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SourcingResultSummary:
    total_num_sourcing_results: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalNumSourcingResults",
            "type": "Element",
        }
    )
    total_num_winning_quotes: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalNumWinningQuotes",
            "type": "Element",
        }
    )
    quote_award_details: List[QuoteAwardDetails] = field(
        default_factory=list,
        metadata={
            "name": "QuoteAwardDetails",
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
class ListOfSourcingResultItem:
    sourcing_result_item: List[SourcingResultItem] = field(
        default_factory=list,
        metadata={
            "name": "SourcingResultItem",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class SourcingResultHeader:
    sourcing_result_purpose: Optional[SourcingResultPurpose] = field(
        default=None,
        metadata={
            "name": "SourcingResultPurpose",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_result_issue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourcingResultIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_result_id: Optional[SourcingResultId] = field(
        default=None,
        metadata={
            "name": "SourcingResultID",
            "type": "Element",
            "required": True,
        }
    )
    tracking_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrackingID",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_create_reference: Optional[SourcingCreateReference] = field(
        default=None,
        metadata={
            "name": "SourcingCreateReference",
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
    sourcing_result_list_of_attachment: Optional[SourcingResultListOfAttachment] = field(
        default=None,
        metadata={
            "name": "SourcingResultListOfAttachment",
            "type": "Element",
        }
    )
    sourcing_result_general_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourcingResultGeneralNote",
            "type": "Element",
        }
    )


@dataclass
class SourcingResultDetail:
    sourcing_result_item_id: Optional[SourcingResultItemId] = field(
        default=None,
        metadata={
            "name": "SourcingResultItemID",
            "type": "Element",
            "required": True,
        }
    )
    winning_quote_indicator: Optional[str] = field(
        default=None,
        metadata={
            "name": "WinningQuoteIndicator",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_result_party: Optional[SourcingResultParty] = field(
        default=None,
        metadata={
            "name": "SourcingResultParty",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_result_dates: Optional[SourcingResultDates] = field(
        default=None,
        metadata={
            "name": "SourcingResultDates",
            "type": "Element",
        }
    )
    sourcing_result_currency: Optional[SourcingResultCurrency] = field(
        default=None,
        metadata={
            "name": "SourcingResultCurrency",
            "type": "Element",
        }
    )
    list_of_sourcing_result_item: Optional[ListOfSourcingResultItem] = field(
        default=None,
        metadata={
            "name": "ListOfSourcingResultItem",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_result_detail_notes: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourcingResultDetailNotes",
            "type": "Element",
        }
    )
    list_of_sourcing_result_detail_attachment: Optional[ListOfSourcingResultDetailAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfSourcingResultDetailAttachment",
            "type": "Element",
        }
    )


@dataclass
class ListOfSourcingResultDetail:
    sourcing_result_detail: List[SourcingResultDetail] = field(
        default_factory=list,
        metadata={
            "name": "SourcingResultDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class SourcingResult:
    sourcing_result_header: Optional[SourcingResultHeader] = field(
        default=None,
        metadata={
            "name": "SourcingResultHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_sourcing_result_detail: Optional[ListOfSourcingResultDetail] = field(
        default=None,
        metadata={
            "name": "ListOfSourcingResultDetail",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_result_summary: Optional[SourcingResultSummary] = field(
        default=None,
        metadata={
            "name": "SourcingResultSummary",
            "type": "Element",
            "required": True,
        }
    )
