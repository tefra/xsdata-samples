from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass(kw_only=True)
class PaymentAdvice3:
    """
    Contains other form of payment for Cruise Reservations.

    Parameters
    ----------
    type_value
        Other Payment Yype. Possible Values: AGC - Agency Check, AGG -
        Agency Guarantee, AWC - Award Check, CSH - Cash Equivalent, DBC -
        Denied Boarding Compensation, MCO - Miscellaneous Charge Order, TOO
        - Tour Order, TOV - Tour Voucher
    document_number
        Payment Document Number Examples: 1234567890, R7777
    issue_date
        Document Issuance date
    issue_city
        City code of document issuance
    original_fop
        Original form of payment Examples: CHECK 3500
    """

    class Meta:
        name = "PaymentAdvice"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    type_value: str = field(
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
            "max_length": 3,
        }
    )
    document_number: str = field(
        metadata={
            "name": "DocumentNumber",
            "type": "Attribute",
            "required": True,
            "max_length": 22,
        }
    )
    issue_date: XmlDate = field(
        metadata={
            "name": "IssueDate",
            "type": "Attribute",
            "required": True,
        }
    )
    issue_city: str = field(
        metadata={
            "name": "IssueCity",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    original_fop: None | str = field(
        default=None,
        metadata={
            "name": "OriginalFOP",
            "type": "Attribute",
            "max_length": 19,
        },
    )
