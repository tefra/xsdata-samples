from dataclasses import dataclass, field
from typing import Optional

from xcbl.models.sourcing_result_response import (
    GeneralNote,
    Purpose,
)
from xcbl.models.trading_partner_response import Reference
from xcbl.models.trading_partner_user_information import Language


@dataclass(kw_only=True)
class AuctionResultResponseCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AuctionResultResponseCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AuctionResultResponseId:
    class Meta:
        name = "AuctionResultResponseID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AuctionResultResponseIssueDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AuctionCreateReference:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


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
    auction_result_response_issue_date: AuctionResultResponseIssueDate = field(
        metadata={
            "name": "AuctionResultResponseIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    auction_result_response_id: AuctionResultResponseId = field(
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
        },
    )
    auction_result_response_coded: AuctionResultResponseCoded = field(
        metadata={
            "name": "AuctionResultResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    auction_result_response_coded_other: Optional[
        AuctionResultResponseCodedOther
    ] = field(
        default=None,
        metadata={
            "name": "AuctionResultResponseCodedOther",
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
    general_note: Optional[GeneralNote] = field(
        default=None,
        metadata={
            "name": "GeneralNote",
            "type": "Element",
        },
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
