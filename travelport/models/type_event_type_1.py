from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


class TypeEventType1(Enum):
    """
    The various reservation events (book, cancel, void, etc)
    """

    CREATE = "Create"
    CANCEL = "Cancel"
    TICKET = "Ticket"
    REFUND = "Refund"
    EXCHANGE = "Exchange"
    VOID = "Void"
