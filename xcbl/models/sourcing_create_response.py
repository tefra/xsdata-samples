from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    Language,
    Purpose,
    Reference,
)


@dataclass
class SourcingCreateSummary:
    total_number_of_sourcing_items: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalNumberOfSourcingItems",
            "type": "Element",
        }
    )
    total_number_of_participants: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalNumberOfParticipants",
            "type": "Element",
        }
    )
    estimated_total_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "EstimatedTotalValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SourcingItemComponentResponse:
    sourcing_create_response_detail: Optional["SourcingCreateResponseDetail"] = field(
        default=None,
        metadata={
            "name": "SourcingCreateResponseDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfSourcingItemComponentResponse:
    sourcing_item_component_response: List[SourcingItemComponentResponse] = field(
        default_factory=list,
        metadata={
            "name": "SourcingItemComponentResponse",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class SourcingCreateReference:
    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SourcingCreateResponsePurpose:
    purpose: Optional[Purpose] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SourcingCreateResponseSummary:
    sourcing_create_summary: Optional[SourcingCreateSummary] = field(
        default=None,
        metadata={
            "name": "SourcingCreateSummary",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SourcingCreateResponseDetail:
    sourcing_item_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourcingItemID",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_item_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourcingItemName",
            "type": "Element",
            "required": True,
        }
    )
    item_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemNumber",
            "type": "Element",
            "required": True,
        }
    )
    parent_item_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParentItemIdentifier",
            "type": "Element",
        }
    )
    sourcing_item_response_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourcingItemResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_item_response_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourcingItemResponseCodedOther",
            "type": "Element",
        }
    )
    list_of_sourcing_item_component_response: Optional[ListOfSourcingItemComponentResponse] = field(
        default=None,
        metadata={
            "name": "ListOfSourcingItemComponentResponse",
            "type": "Element",
        }
    )


@dataclass
class SourcingCreateResponseHeader:
    sourcing_create_response_purpose: Optional[SourcingCreateResponsePurpose] = field(
        default=None,
        metadata={
            "name": "SourcingCreateResponsePurpose",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_create_response_issue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourcingCreateResponseIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_create_response_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourcingCreateResponseID",
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
    tracking_idnumber: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrackingIDNumber",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_response_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourcingResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_response_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourcingResponseCodedOther",
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
    sourcing_create_response_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourcingCreateResponseNote",
            "type": "Element",
        }
    )


@dataclass
class ListOfSourcingCreateResponseDetail:
    sourcing_create_response_detail: List[SourcingCreateResponseDetail] = field(
        default_factory=list,
        metadata={
            "name": "SourcingCreateResponseDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class SourcingCreateResponse:
    sourcing_create_response_header: Optional[SourcingCreateResponseHeader] = field(
        default=None,
        metadata={
            "name": "SourcingCreateResponseHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_sourcing_create_response_detail: Optional[ListOfSourcingCreateResponseDetail] = field(
        default=None,
        metadata={
            "name": "ListOfSourcingCreateResponseDetail",
            "type": "Element",
        }
    )
    sourcing_create_response_summary: Optional[SourcingCreateResponseSummary] = field(
        default=None,
        metadata={
            "name": "SourcingCreateResponseSummary",
            "type": "Element",
        }
    )
