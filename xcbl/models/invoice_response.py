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


@dataclass(kw_only=True)
class InvoiceReference:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class InvoiceResponseDetail:
    line_item_num: LineItemNum = field(
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


@dataclass(kw_only=True)
class InvoicingParty:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class InvoiceResponseParty:
    invoicing_party: InvoicingParty = field(
        metadata={
            "name": "InvoicingParty",
            "type": "Element",
            "required": True,
        }
    )
    bill_to_party: BillToParty = field(
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


@dataclass(kw_only=True)
class ListOfInvoiceResponseDetail:
    invoice_response_detail: List[InvoiceResponseDetail] = field(
        default_factory=list,
        metadata={
            "name": "InvoiceResponseDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class InvoiceResponseHeader:
    buyer_invoice_number: str = field(
        metadata={
            "name": "BuyerInvoiceNumber",
            "type": "Element",
            "required": True,
        }
    )
    invoice_reference: InvoiceReference = field(
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
    invoice_type: InvoiceType = field(
        metadata={
            "name": "InvoiceType",
            "type": "Element",
            "required": True,
        }
    )
    language: Language = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )
    invoice_response_coded: str = field(
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
    invoice_response_party: InvoiceResponseParty = field(
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


@dataclass(kw_only=True)
class InvoiceResponse:
    invoice_response_header: InvoiceResponseHeader = field(
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
