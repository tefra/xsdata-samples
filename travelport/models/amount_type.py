from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/passive_v52_0"


class AmountType(Enum):
    """
    Properties
    ----------
    DUE
        Amount is Due
    PAID
        Amount is Paid
    TEXT
        Amount field has text.
    """

    DUE = "Due"
    PAID = "Paid"
    TEXT = "Text"
