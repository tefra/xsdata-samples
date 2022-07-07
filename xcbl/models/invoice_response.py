from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    Language,
    ListOfAttachment,
    Party,
    Reference,
)
from xcbl.models.invoice import InvoiceType
from xcbl.models.order_request import (
    BillToParty,
    LineItemNum,
    ListOfNameValueSet,
    ListOfPartyCoded,
    ListOfStructuredNote,
    RemitToParty,
)
from xcbl.models.order_status_result import ErrorInfo


@dataclass
class InvoiceReference:
    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class InvoiceResponseDetail:
    line_item_num: Optional[LineItemNum] = field(
        default=None,
        metadata={
            "name": "LineItemNum",
            "type": "Element",
            "required": True,
        }
    )
    invoice_response_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "InvoiceResponseCoded",
            "type": "Element",
        }
    )
    invoice_response_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "InvoiceResponseCodedOther",
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
    error_info: Optional[ErrorInfo] = field(
        default=None,
        metadata={
            "name": "ErrorInfo",
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
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
        }
    )


@dataclass
class InvoicingParty:
    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class InvoiceResponseParty:
    invoicing_party: Optional[InvoicingParty] = field(
        default=None,
        metadata={
            "name": "InvoicingParty",
            "type": "Element",
            "required": True,
        }
    )
    bill_to_party: Optional[BillToParty] = field(
        default=None,
        metadata={
            "name": "BillToParty",
            "type": "Element",
            "required": True,
        }
    )
    remit_to_party: Optional[RemitToParty] = field(
        default=None,
        metadata={
            "name": "RemitToParty",
            "type": "Element",
        }
    )
    list_of_party_coded: Optional[ListOfPartyCoded] = field(
        default=None,
        metadata={
            "name": "ListOfPartyCoded",
            "type": "Element",
        }
    )


@dataclass
class ListOfInvoiceResponseDetail:
    invoice_response_detail: List[InvoiceResponseDetail] = field(
        default_factory=list,
        metadata={
            "name": "InvoiceResponseDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class InvoiceResponseHeader:
    buyer_invoice_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "BuyerInvoiceNumber",
            "type": "Element",
            "required": True,
        }
    )
    invoice_reference: Optional[InvoiceReference] = field(
        default=None,
        metadata={
            "name": "InvoiceReference",
            "type": "Element",
            "required": True,
        }
    )
    invoice_response_issue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "InvoiceResponseIssueDate",
            "type": "Element",
        }
    )
    invoice_type: Optional[InvoiceType] = field(
        default=None,
        metadata={
            "name": "InvoiceType",
            "type": "Element",
            "required": True,
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
    invoice_response_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "InvoiceResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    invoice_response_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "InvoiceResponseCodedOther",
            "type": "Element",
        }
    )
    invoice_response_party: Optional[InvoiceResponseParty] = field(
        default=None,
        metadata={
            "name": "InvoiceResponseParty",
            "type": "Element",
            "required": True,
        }
    )
    invoice_response_header_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "InvoiceResponseHeaderNote",
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
    error_info: Optional[ErrorInfo] = field(
        default=None,
        metadata={
            "name": "ErrorInfo",
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
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
        }
    )


@dataclass
class InvoiceResponse:
    invoice_response_header: Optional[InvoiceResponseHeader] = field(
        default=None,
        metadata={
            "name": "InvoiceResponseHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_invoice_response_detail: Optional[ListOfInvoiceResponseDetail] = field(
        default=None,
        metadata={
            "name": "ListOfInvoiceResponseDetail",
            "type": "Element",
        }
    )
