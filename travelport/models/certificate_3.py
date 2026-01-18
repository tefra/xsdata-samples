from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass(kw_only=True)
class Certificate3:
    """
    Certificate Form of Payment.

    Parameters
    ----------
    number
        The Certificate number
    amount
        The monetary value of the certificate.
    discount_amount
        The monetary discount amount of this certificate.
    discount_percentage
        The percentage discount value of this certificate.
    not_valid_before
        The date that this certificate becomes valid.
    not_valid_after
        The date that this certificate expires.
    """

    class Meta:
        name = "Certificate"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    number: str = field(
        metadata={
            "name": "Number",
            "type": "Attribute",
            "required": True,
        }
    )
    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        },
    )
    discount_amount: None | str = field(
        default=None,
        metadata={
            "name": "DiscountAmount",
            "type": "Attribute",
        },
    )
    discount_percentage: None | int = field(
        default=None,
        metadata={
            "name": "DiscountPercentage",
            "type": "Attribute",
        },
    )
    not_valid_before: None | XmlDate = field(
        default=None,
        metadata={
            "name": "NotValidBefore",
            "type": "Attribute",
        },
    )
    not_valid_after: None | XmlDate = field(
        default=None,
        metadata={
            "name": "NotValidAfter",
            "type": "Attribute",
        },
    )
