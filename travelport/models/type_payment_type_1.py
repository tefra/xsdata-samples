from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


class TypePaymentType1(StrEnum):
    """
    Defines the form of payment type. (Credit Card, Cash, etc).
    """

    CREDIT_CARD = "Credit Card"
    DEBIT_CARD = "Debit Card"
