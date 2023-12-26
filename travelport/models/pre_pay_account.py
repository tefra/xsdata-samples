from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate
from travelport.models.credit_summary import CreditSummary
from travelport.models.pre_pay_price_info import PrePayPriceInfo

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class PrePayAccount:
    """
    PrePay Account associated with the customer.

    Parameters
    ----------
    credit_summary
    pre_pay_price_info
    program_title
        Pre pay program title
    certificate_number
    program_name
        Pre pay program name
    effective_date
        Effective date for the pre pay account
    expire_date
        Expiry date for the pre pay account
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    credit_summary: None | CreditSummary = field(
        default=None,
        metadata={
            "name": "CreditSummary",
            "type": "Element",
        },
    )
    pre_pay_price_info: None | PrePayPriceInfo = field(
        default=None,
        metadata={
            "name": "PrePayPriceInfo",
            "type": "Element",
        },
    )
    program_title: None | str = field(
        default=None,
        metadata={
            "name": "ProgramTitle",
            "type": "Attribute",
        },
    )
    certificate_number: None | str = field(
        default=None,
        metadata={
            "name": "CertificateNumber",
            "type": "Attribute",
        },
    )
    program_name: None | str = field(
        default=None,
        metadata={
            "name": "ProgramName",
            "type": "Attribute",
        },
    )
    effective_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "EffectiveDate",
            "type": "Attribute",
        },
    )
    expire_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "ExpireDate",
            "type": "Attribute",
        },
    )
