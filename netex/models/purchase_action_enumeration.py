from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PurchaseActionEnumeration(StrEnum):
    PURCHASE = "purchase"
    ORDER_WITHOUT_PAYMENT = "orderWithoutPayment"
    RESERVE = "reserve"
    PAY_FOR_PREVIOUS_ORDER = "payForPreviousOrder"
    SUBSCRIBE = "subscribe"
    PAY_INSTALLMENT = "payInstallment"
    OTHER = "other"
