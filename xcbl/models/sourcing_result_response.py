from __future__ import annotations

from dataclasses import dataclass, field

from xcbl.models.trading_partner_response import Reference
from xcbl.models.trading_partner_user_information import Language


@dataclass(kw_only=True)
class GeneralNote:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PurposeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PurposeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SourcingResultResponseCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SourcingResultResponseCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SourcingResultResponseId:
    class Meta:
        name = "SourcingResultResponseID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SourcingresultResponseissueDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TrackingId:
    class Meta:
        name = "TrackingID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Purpose:
    purpose_coded: PurposeCoded = field(
        metadata={
            "name": "PurposeCoded",
            "type": "Element",
            "required": True,
        }
    )
    purpose_coded_other: PurposeCodedOther | None = field(
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
    sourcingresult_responseissue_date: SourcingresultResponseissueDate = field(
        metadata={
            "name": "SourcingresultResponseissueDate",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_result_response_id: SourcingResultResponseId = field(
        metadata={
            "name": "SourcingResultResponseID",
            "type": "Element",
            "required": True,
        }
    )
    tracking_id: TrackingId = field(
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
    sourcing_result_reference: SourcingResultReference | None = field(
        default=None,
        metadata={
            "name": "SourcingResultReference",
            "type": "Element",
        },
    )
    sourcing_result_response_coded: SourcingResultResponseCoded = field(
        metadata={
            "name": "SourcingResultResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_result_response_coded_other: (
        SourcingResultResponseCodedOther | None
    ) = field(
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
    general_note: GeneralNote | None = field(
        default=None,
        metadata={
            "name": "GeneralNote",
            "type": "Element",
        },
    )
