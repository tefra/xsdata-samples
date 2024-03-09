from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


class TypeCommissionCategory1(Enum):
    """A type that represents a category of commissions.

    Example include per booking, by monetary amount, etc.
    """

    PER_BOOKING = "Per Booking"
    PER_PERSON = "Per Person"
    PER_TICKET = "Per Ticket"
