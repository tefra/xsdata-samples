from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


class TypeFulfillmentIdtype5(StrEnum):
    """
    IdentificationType to define how the customer will identify himself
    when collecting the ticket.
    """

    BAHN_CARD = "Bahn Card"
    CREDIT_CARD = "Credit Card"
    EURO_CHEQUE_CARD = "Euro Cheque Card"
    COLLECTION_REFERENCE = "Collection Reference"
