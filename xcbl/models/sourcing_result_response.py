from dataclasses import dataclass, field
from typing import Optional
from xcbl.models.auction_create import (
    Language,
    Purpose,
    Reference,
)
from xcbl.models.sourcing_create_response import SourcingCreateReference


@dataclass
class SourcingResultReference:
    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SourcingResultResponsePurpose:
    purpose: Optional[Purpose] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SourcingResultResponse:
    sourcing_result_response_purpose: Optional[SourcingResultResponsePurpose] = field(
        default=None,
        metadata={
            "name": "SourcingResultResponsePurpose",
            "type": "Element",
            "required": True,
        }
    )
    sourcingresult_responseissue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourcingresultResponseissueDate",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_result_response_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourcingResultResponseID",
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
    sourcing_result_reference: Optional[SourcingResultReference] = field(
        default=None,
        metadata={
            "name": "SourcingResultReference",
            "type": "Element",
        }
    )
    sourcing_result_response_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourcingResultResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_result_response_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourcingResultResponseCodedOther",
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
