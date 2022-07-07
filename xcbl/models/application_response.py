from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    Party,
    Reference,
)
from xcbl.models.order_request import (
    LineItemNumberReference,
    ListOfNameValueSet,
    ListOfStructuredNote,
)
from xcbl.models.order_status_result import ErrorInfo


@dataclass
class ApplicationIdentification:
    application_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApplicationID",
            "type": "Element",
            "required": True,
        }
    )
    application_idextension: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApplicationIDExtension",
            "type": "Element",
        }
    )
    application_instance: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApplicationInstance",
            "type": "Element",
        }
    )


@dataclass
class ApplicationResponseReceiver:
    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ApplicationResponseSender:
    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class DocumentReference:
    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ItemReference:
    line_item_number_reference: Optional[LineItemNumberReference] = field(
        default=None,
        metadata={
            "name": "LineItemNumberReference",
            "type": "Element",
            "required": True,
        }
    )
    schedule_line_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ScheduleLineID",
            "type": "Element",
        }
    )


@dataclass
class RespondingApplication:
    application_identification: Optional[ApplicationIdentification] = field(
        default=None,
        metadata={
            "name": "ApplicationIdentification",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SendingApplication:
    application_identification: Optional[ApplicationIdentification] = field(
        default=None,
        metadata={
            "name": "ApplicationIdentification",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ApplicationResponseDetail:
    error_type_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ErrorTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    error_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ErrorTypeCodedOther",
            "type": "Element",
        }
    )
    item_reference: Optional[ItemReference] = field(
        default=None,
        metadata={
            "name": "ItemReference",
            "type": "Element",
        }
    )
    error_info: Optional[ErrorInfo] = field(
        default=None,
        metadata={
            "name": "ErrorInfo",
            "type": "Element",
            "required": True,
        }
    )
    list_of_structured_note: Optional[ListOfStructuredNote] = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        }
    )
    list_of_name_value_set: Optional[ListOfNameValueSet] = field(
        default=None,
        metadata={
            "name": "ListOfNameValueSet",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ApplicationResponseHeader:
    application_response_issue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApplicationResponseIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    application_response_type_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApplicationResponseTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    application_response_sender: Optional[ApplicationResponseSender] = field(
        default=None,
        metadata={
            "name": "ApplicationResponseSender",
            "type": "Element",
            "required": True,
        }
    )
    sending_application: Optional[SendingApplication] = field(
        default=None,
        metadata={
            "name": "SendingApplication",
            "type": "Element",
        }
    )
    application_response_receiver: Optional[ApplicationResponseReceiver] = field(
        default=None,
        metadata={
            "name": "ApplicationResponseReceiver",
            "type": "Element",
            "required": True,
        }
    )
    responding_application: Optional[RespondingApplication] = field(
        default=None,
        metadata={
            "name": "RespondingApplication",
            "type": "Element",
        }
    )
    business_document_type_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "BusinessDocumentTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    business_document_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "BusinessDocumentTypeCodedOther",
            "type": "Element",
        }
    )
    document_reference: Optional[DocumentReference] = field(
        default=None,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "required": True,
        }
    )
    document_status_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocumentStatusCoded",
            "type": "Element",
            "required": True,
        }
    )
    document_status_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocumentStatusCodedOther",
            "type": "Element",
        }
    )
    application_response_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApplicationResponseNote",
            "type": "Element",
        }
    )
    list_of_structured_note: Optional[ListOfStructuredNote] = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        }
    )
    list_of_name_value_set: Optional[ListOfNameValueSet] = field(
        default=None,
        metadata={
            "name": "ListOfNameValueSet",
            "type": "Element",
        }
    )


@dataclass
class ListOfApplicationResponseDetail:
    application_response_detail: List[ApplicationResponseDetail] = field(
        default_factory=list,
        metadata={
            "name": "ApplicationResponseDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ApplicationResponse:
    application_response_header: Optional[ApplicationResponseHeader] = field(
        default=None,
        metadata={
            "name": "ApplicationResponseHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_application_response_detail: Optional[ListOfApplicationResponseDetail] = field(
        default=None,
        metadata={
            "name": "ListOfApplicationResponseDetail",
            "type": "Element",
        }
    )
