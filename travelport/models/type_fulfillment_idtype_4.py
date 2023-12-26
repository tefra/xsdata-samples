from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


class TypeFulfillmentIdtype4(Enum):
    """
    IdentificationType to define how the customer will identify himself when
    collecting the ticket.
    """

    BAHN_CARD = "Bahn Card"
    CREDIT_CARD = "Credit Card"
    EURO_CHEQUE_CARD = "Euro Cheque Card"
    COLLECTION_REFERENCE = "Collection Reference"
