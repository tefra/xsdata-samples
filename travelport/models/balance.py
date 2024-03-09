from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.travelport.com/schema/cruise_v52_0"


@dataclass
class Balance:
    """
    Indicates balance dates.

    Parameters
    ----------
    due_date
        Date when deposit or balance is due.
    received_date
        Date when deposit or balance is received, if received.
    credit_card_due_amount
        Balance due via credit card payment
    check_due_amount
        Balance due via personal check
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/cruise_v52_0"

    due_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "DueDate",
            "type": "Attribute",
        },
    )
    received_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "ReceivedDate",
            "type": "Attribute",
        },
    )
    credit_card_due_amount: None | str = field(
        default=None,
        metadata={
            "name": "CreditCardDueAmount",
            "type": "Attribute",
        },
    )
    check_due_amount: None | str = field(
        default=None,
        metadata={
            "name": "CheckDueAmount",
            "type": "Attribute",
        },
    )
