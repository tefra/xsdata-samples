from __future__ import annotations

from dataclasses import dataclass, field

from xcbl.models.price_check_result import ErrorInfo
from xcbl.models.remittance_advice import InvoiceType
from xcbl.models.sourcing_result import (
    BillToParty,
    LineItemNum,
    ListOfAttachment,
    ListOfNameValueSet,
    ListOfStructuredNote,
    RemitToParty,
)
from xcbl.models.time_series_response import (
    ListOfPartyCoded,
    Party,
)
from xcbl.models.trading_partner_response import Reference
from xcbl.models.trading_partner_user_information import Language


@dataclass(kw_only=True)
class BuyerInvoiceNumber:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class InvoiceResponseCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class InvoiceResponseCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class InvoiceResponseHeaderNote:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class InvoiceResponseIssueDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


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
    invoice_response_coded: InvoiceResponseCoded | None = field(
        default=None,
        metadata={
            "name": "InvoiceResponseCoded",
            "type": "Element",
        },
    )
    invoice_response_coded_other: InvoiceResponseCodedOther | None = field(
        default=None,
        metadata={
            "name": "InvoiceResponseCodedOther",
            "type": "Element",
        },
    )
    list_of_structured_note: ListOfStructuredNote | None = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        },
    )
    error_info: ErrorInfo | None = field(
        default=None,
        metadata={
            "name": "ErrorInfo",
            "type": "Element",
        },
    )
    list_of_name_value_set: ListOfNameValueSet | None = field(
        default=None,
        metadata={
            "name": "ListOfNameValueSet",
            "type": "Element",
        },
    )
    list_of_attachment: ListOfAttachment | None = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
        },
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
    remit_to_party: RemitToParty | None = field(
        default=None,
        metadata={
            "name": "RemitToParty",
            "type": "Element",
        },
    )
    list_of_party_coded: ListOfPartyCoded | None = field(
        default=None,
        metadata={
            "name": "ListOfPartyCoded",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfInvoiceResponseDetail:
    invoice_response_detail: list[InvoiceResponseDetail] = field(
        default_factory=list,
        metadata={
            "name": "InvoiceResponseDetail",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class InvoiceResponseHeader:
    buyer_invoice_number: BuyerInvoiceNumber = field(
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
    invoice_response_issue_date: InvoiceResponseIssueDate | None = field(
        default=None,
        metadata={
            "name": "InvoiceResponseIssueDate",
            "type": "Element",
        },
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
    invoice_response_coded: InvoiceResponseCoded = field(
        metadata={
            "name": "InvoiceResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    invoice_response_coded_other: InvoiceResponseCodedOther | None = field(
        default=None,
        metadata={
            "name": "InvoiceResponseCodedOther",
            "type": "Element",
        },
    )
    invoice_response_party: InvoiceResponseParty = field(
        metadata={
            "name": "InvoiceResponseParty",
            "type": "Element",
            "required": True,
        }
    )
    invoice_response_header_note: InvoiceResponseHeaderNote | None = field(
        default=None,
        metadata={
            "name": "InvoiceResponseHeaderNote",
            "type": "Element",
        },
    )
    list_of_structured_note: ListOfStructuredNote | None = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        },
    )
    error_info: ErrorInfo | None = field(
        default=None,
        metadata={
            "name": "ErrorInfo",
            "type": "Element",
        },
    )
    list_of_name_value_set: ListOfNameValueSet | None = field(
        default=None,
        metadata={
            "name": "ListOfNameValueSet",
            "type": "Element",
        },
    )
    list_of_attachment: ListOfAttachment | None = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
        },
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
    list_of_invoice_response_detail: ListOfInvoiceResponseDetail | None = (
        field(
            default=None,
            metadata={
                "name": "ListOfInvoiceResponseDetail",
                "type": "Element",
            },
        )
    )
