from dataclasses import dataclass, field
from typing import Optional
from xcbl.models.auction_create import (
    Language,
    Purpose,
    Reference,
)
from xcbl.models.auction_result import AuctionCreateReference


@dataclass(kw_only=True)
class AuctionResultReference:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AuctionResultResponsePurpose:
    purpose: Purpose = field(
        metadata={
            "name": "Purpose",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AuctionResultResponseHeader:
    auction_result_response_purpose: AuctionResultResponsePurpose = field(
        metadata={
            "name": "AuctionResultResponsePurpose",
            "type": "Element",
            "required": True,
        }
    )
    auction_result_response_issue_date: str = field(
        metadata={
            "name": "AuctionResultResponseIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    auction_result_response_id: str = field(
        metadata={
            "name": "AuctionResultResponseID",
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
    auction_result_reference: Optional[AuctionResultReference] = field(
        default=None,
        metadata={
            "name": "AuctionResultReference",
            "type": "Element",
        }
    )
    auction_result_response_coded: str = field(
        metadata={
            "name": "AuctionResultResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    auction_result_response_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionResultResponseCodedOther",
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
    general_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeneralNote",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class AuctionResultResponse:
    auction_result_response_header: AuctionResultResponseHeader = field(
        metadata={
            "name": "AuctionResultResponseHeader",
            "type": "Element",
            "required": True,
        }
    )
