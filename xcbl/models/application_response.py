from __future__ import annotations

from dataclasses import dataclass, field

from xcbl.models.price_check_result import ErrorInfo
from xcbl.models.sourcing_result import (
    LineItemNumberReference,
    ListOfNameValueSet,
    ListOfStructuredNote,
    ScheduleLineId,
)
from xcbl.models.time_series_response import Party
from xcbl.models.trading_partner_response import Reference


@dataclass(kw_only=True)
class ApplicationId:
    class Meta:
        name = "ApplicationID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ApplicationIdextension:
    class Meta:
        name = "ApplicationIDExtension"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ApplicationInstance:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ApplicationResponseIssueDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ApplicationResponseNote:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ApplicationResponseTypeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class BusinessDocumentTypeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class BusinessDocumentTypeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class DocumentStatusCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class DocumentStatusCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ErrorTypeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ErrorTypeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ApplicationIdentification:
    application_id: ApplicationId = field(
        metadata={
            "name": "ApplicationID",
            "type": "Element",
            "required": True,
        }
    )
    application_idextension: None | ApplicationIdextension = field(
        default=None,
        metadata={
            "name": "ApplicationIDExtension",
            "type": "Element",
        },
    )
    application_instance: None | ApplicationInstance = field(
        default=None,
        metadata={
            "name": "ApplicationInstance",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ApplicationResponseReceiver:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ApplicationResponseSender:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class DocumentReference:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ItemReference:
    line_item_number_reference: LineItemNumberReference = field(
        metadata={
            "name": "LineItemNumberReference",
            "type": "Element",
            "required": True,
        }
    )
    schedule_line_id: None | ScheduleLineId = field(
        default=None,
        metadata={
            "name": "ScheduleLineID",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ApplicationResponseDetail:
    error_type_coded: ErrorTypeCoded = field(
        metadata={
            "name": "ErrorTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    error_type_coded_other: None | ErrorTypeCodedOther = field(
        default=None,
        metadata={
            "name": "ErrorTypeCodedOther",
            "type": "Element",
        },
    )
    item_reference: None | ItemReference = field(
        default=None,
        metadata={
            "name": "ItemReference",
            "type": "Element",
        },
    )
    error_info: ErrorInfo = field(
        metadata={
            "name": "ErrorInfo",
            "type": "Element",
            "required": True,
        }
    )
    list_of_structured_note: None | ListOfStructuredNote = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        },
    )
    list_of_name_value_set: ListOfNameValueSet = field(
        metadata={
            "name": "ListOfNameValueSet",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RespondingApplication:
    application_identification: ApplicationIdentification = field(
        metadata={
            "name": "ApplicationIdentification",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SendingApplication:
    application_identification: ApplicationIdentification = field(
        metadata={
            "name": "ApplicationIdentification",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ApplicationResponseHeader:
    application_response_issue_date: ApplicationResponseIssueDate = field(
        metadata={
            "name": "ApplicationResponseIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    application_response_type_coded: ApplicationResponseTypeCoded = field(
        metadata={
            "name": "ApplicationResponseTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    application_response_sender: ApplicationResponseSender = field(
        metadata={
            "name": "ApplicationResponseSender",
            "type": "Element",
            "required": True,
        }
    )
    sending_application: None | SendingApplication = field(
        default=None,
        metadata={
            "name": "SendingApplication",
            "type": "Element",
        },
    )
    application_response_receiver: ApplicationResponseReceiver = field(
        metadata={
            "name": "ApplicationResponseReceiver",
            "type": "Element",
            "required": True,
        }
    )
    responding_application: None | RespondingApplication = field(
        default=None,
        metadata={
            "name": "RespondingApplication",
            "type": "Element",
        },
    )
    business_document_type_coded: BusinessDocumentTypeCoded = field(
        metadata={
            "name": "BusinessDocumentTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    business_document_type_coded_other: (
        None | BusinessDocumentTypeCodedOther
    ) = field(
        default=None,
        metadata={
            "name": "BusinessDocumentTypeCodedOther",
            "type": "Element",
        },
    )
    document_reference: DocumentReference = field(
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "required": True,
        }
    )
    document_status_coded: DocumentStatusCoded = field(
        metadata={
            "name": "DocumentStatusCoded",
            "type": "Element",
            "required": True,
        }
    )
    document_status_coded_other: None | DocumentStatusCodedOther = field(
        default=None,
        metadata={
            "name": "DocumentStatusCodedOther",
            "type": "Element",
        },
    )
    application_response_note: None | ApplicationResponseNote = field(
        default=None,
        metadata={
            "name": "ApplicationResponseNote",
            "type": "Element",
        },
    )
    list_of_structured_note: None | ListOfStructuredNote = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        },
    )
    list_of_name_value_set: None | ListOfNameValueSet = field(
        default=None,
        metadata={
            "name": "ListOfNameValueSet",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfApplicationResponseDetail:
    application_response_detail: list[ApplicationResponseDetail] = field(
        default_factory=list,
        metadata={
            "name": "ApplicationResponseDetail",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ApplicationResponse:
    application_response_header: ApplicationResponseHeader = field(
        metadata={
            "name": "ApplicationResponseHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_application_response_detail: (
        None | ListOfApplicationResponseDetail
    ) = field(
        default=None,
        metadata={
            "name": "ListOfApplicationResponseDetail",
            "type": "Element",
        },
    )
