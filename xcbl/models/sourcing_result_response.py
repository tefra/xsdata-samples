from dataclasses import dataclass, field
from typing import Optional
from xcbl.models.trading_partner_response import Reference
from xcbl.models.trading_partner_user_information import Language


@dataclass(kw_only=True)
class Purpose:
    purpose_coded: str = field(
        metadata={
            "name": "PurposeCoded",
            "type": "Element",
            "required": True,
        }
    )
    purpose_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "PurposeCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class SourcingCreateReference:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SourcingResultReference:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SourcingResultResponsePurpose:
    purpose: Purpose = field(
        metadata={
            "name": "Purpose",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SourcingResultResponse:
    sourcing_result_response_purpose: SourcingResultResponsePurpose = field(
        metadata={
            "name": "SourcingResultResponsePurpose",
            "type": "Element",
            "required": True,
        }
    )
    sourcingresult_responseissue_date: str = field(
        metadata={
            "name": "SourcingresultResponseissueDate",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_result_response_id: str = field(
        metadata={
            "name": "SourcingResultResponseID",
            "type": "Element",
            "required": True,
        }
    )
    tracking_id: str = field(
        metadata={
            "name": "TrackingID",
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
    sourcing_result_reference: Optional[SourcingResultReference] = field(
        default=None,
        metadata={
            "name": "SourcingResultReference",
            "type": "Element",
        },
    )
    sourcing_result_response_coded: str = field(
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
        },
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
        },
    )
