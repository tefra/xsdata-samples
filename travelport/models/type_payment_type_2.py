from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


class TypePaymentType2(Enum):
    """Defines the form of payment type.

    (Credit Card, Cash, etc)
    """

    CREDIT_CARD = "Credit Card"
    DEBIT_CARD = "Debit Card"
