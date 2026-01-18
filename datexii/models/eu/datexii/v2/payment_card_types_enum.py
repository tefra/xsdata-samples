from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class PaymentCardTypesEnum(Enum):
    """
    Types of payment cards.

    :cvar CREDIT_CARD: Credit card
    :cvar DEBIT_CARD: Debit card
    :cvar CHARGE_CARD: Charge card
    :cvar FLEET_CARD: Fleet or petrol station card.
    :cvar STORED_VALUE_CARD: Stored value card / prepaid card.
    :cvar OTHER: Some other type of card.
    """

    CREDIT_CARD = "creditCard"
    DEBIT_CARD = "debitCard"
    CHARGE_CARD = "chargeCard"
    FLEET_CARD = "fleetCard"
    STORED_VALUE_CARD = "storedValueCard"
    OTHER = "other"
