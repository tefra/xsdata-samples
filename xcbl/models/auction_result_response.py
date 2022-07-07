from dataclasses import dataclass, field
from typing import Optional
from xcbl.models.auction_create import (
    Language,
    Purpose,
    Reference,
)
from xcbl.models.auction_result import AuctionCreateReference


@dataclass
class AuctionResultReference:
    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AuctionResultResponsePurpose:
    purpose: Optional[Purpose] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AuctionResultResponseHeader:
    auction_result_response_purpose: Optional[AuctionResultResponsePurpose] = field(
        default=None,
        metadata={
            "name": "AuctionResultResponsePurpose",
            "type": "Element",
            "required": True,
        }
    )
    auction_result_response_issue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionResultResponseIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    auction_result_response_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionResultResponseID",
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
    auction_result_reference: Optional[AuctionResultReference] = field(
        default=None,
        metadata={
            "name": "AuctionResultReference",
            "type": "Element",
        }
    )
    auction_result_response_coded: Optional[str] = field(
        default=None,
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
    language: Optional[Language] = field(
        default=None,
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


@dataclass
class AuctionResultResponse:
    auction_result_response_header: Optional[AuctionResultResponseHeader] = field(
        default=None,
        metadata={
            "name": "AuctionResultResponseHeader",
            "type": "Element",
            "required": True,
        }
    )
