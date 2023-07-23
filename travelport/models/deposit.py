from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.travelport.com/schema/cruise_v52_0"


@dataclass
class Deposit:
    """
    Indicates Deposit dates.

    Parameters
    ----------
    amount
        Amount of Deposit
    due_date
        Date when deposit or balance is due.
    received_date
        Date when deposit or balance is received, if received.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/cruise_v52_0"

    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        }
    )
    due_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "DueDate",
            "type": "Attribute",
        }
    )
    received_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "ReceivedDate",
            "type": "Attribute",
        }
    )
