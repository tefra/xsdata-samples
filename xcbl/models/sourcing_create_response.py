from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.sourcing_result_response import (
    Purpose,
    SourcingCreateReference,
)
from xcbl.models.trading_partner_user_information import Language


@dataclass(kw_only=True)
class EstimatedTotalValue:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ItemNumber:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ParentItemIdentifier:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SourcingCreateResponseId:
    class Meta:
        name = "SourcingCreateResponseID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SourcingCreateResponseIssueDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SourcingCreateResponseNote:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SourcingItemId:
    class Meta:
        name = "SourcingItemID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SourcingItemName:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SourcingItemResponseCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SourcingItemResponseCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SourcingResponseCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SourcingResponseCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TotalNumberOfParticipants:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TotalNumberOfSourcingItems:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TrackingIdnumber:
    class Meta:
        name = "TrackingIDNumber"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SourcingCreateResponseDetail:
    sourcing_item_id: SourcingItemId = field(
        metadata={
            "name": "SourcingItemID",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_item_name: SourcingItemName = field(
        metadata={
            "name": "SourcingItemName",
            "type": "Element",
            "required": True,
        }
    )
    item_number: ItemNumber = field(
        metadata={
            "name": "ItemNumber",
            "type": "Element",
            "required": True,
        }
    )
    parent_item_identifier: Optional[ParentItemIdentifier] = field(
        default=None,
        metadata={
            "name": "ParentItemIdentifier",
            "type": "Element",
        },
    )
    sourcing_item_response_coded: SourcingItemResponseCoded = field(
        metadata={
            "name": "SourcingItemResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_item_response_coded_other: Optional[
        SourcingItemResponseCodedOther
    ] = field(
        default=None,
        metadata={
            "name": "SourcingItemResponseCodedOther",
            "type": "Element",
        },
    )
    list_of_sourcing_item_component_response: Optional[
        "ListOfSourcingItemComponentResponse"
    ] = field(
        default=None,
        metadata={
            "name": "ListOfSourcingItemComponentResponse",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class SourcingCreateResponsePurpose:
    purpose: Purpose = field(
        metadata={
            "name": "Purpose",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SourcingCreateSummary:
    total_number_of_sourcing_items: Optional[
        TotalNumberOfSourcingItems
    ] = field(
        default=None,
        metadata={
            "name": "TotalNumberOfSourcingItems",
            "type": "Element",
        },
    )
    total_number_of_participants: Optional[TotalNumberOfParticipants] = field(
        default=None,
        metadata={
            "name": "TotalNumberOfParticipants",
            "type": "Element",
        },
    )
    estimated_total_value: EstimatedTotalValue = field(
        metadata={
            "name": "EstimatedTotalValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfSourcingCreateResponseDetail:
    sourcing_create_response_detail: List[
        SourcingCreateResponseDetail
    ] = field(
        default_factory=list,
        metadata={
            "name": "SourcingCreateResponseDetail",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class SourcingCreateResponseHeader:
    sourcing_create_response_purpose: SourcingCreateResponsePurpose = field(
        metadata={
            "name": "SourcingCreateResponsePurpose",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_create_response_issue_date: SourcingCreateResponseIssueDate = (
        field(
            metadata={
                "name": "SourcingCreateResponseIssueDate",
                "type": "Element",
                "required": True,
            }
        )
    )
    sourcing_create_response_id: SourcingCreateResponseId = field(
        metadata={
            "name": "SourcingCreateResponseID",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_create_reference: SourcingCreateReference = field(
        metadata={
            "name": "SourcingCreateReference",
            "type": "Element",
            "required": True,
        }
    )
    tracking_idnumber: TrackingIdnumber = field(
        metadata={
            "name": "TrackingIDNumber",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_response_coded: SourcingResponseCoded = field(
        metadata={
            "name": "SourcingResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_response_coded_other: Optional[
        SourcingResponseCodedOther
    ] = field(
        default=None,
        metadata={
            "name": "SourcingResponseCodedOther",
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
    sourcing_create_response_note: Optional[
        SourcingCreateResponseNote
    ] = field(
        default=None,
        metadata={
            "name": "SourcingCreateResponseNote",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class SourcingCreateResponseSummary:
    sourcing_create_summary: SourcingCreateSummary = field(
        metadata={
            "name": "SourcingCreateSummary",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SourcingItemComponentResponse:
    sourcing_create_response_detail: SourcingCreateResponseDetail = field(
        metadata={
            "name": "SourcingCreateResponseDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfSourcingItemComponentResponse:
    sourcing_item_component_response: List[
        SourcingItemComponentResponse
    ] = field(
        default_factory=list,
        metadata={
            "name": "SourcingItemComponentResponse",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class SourcingCreateResponse:
    sourcing_create_response_header: SourcingCreateResponseHeader = field(
        metadata={
            "name": "SourcingCreateResponseHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_sourcing_create_response_detail: Optional[
        ListOfSourcingCreateResponseDetail
    ] = field(
        default=None,
        metadata={
            "name": "ListOfSourcingCreateResponseDetail",
            "type": "Element",
        },
    )
    sourcing_create_response_summary: Optional[
        SourcingCreateResponseSummary
    ] = field(
        default=None,
        metadata={
            "name": "SourcingCreateResponseSummary",
            "type": "Element",
        },
    )
