from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeEticketability(Enum):
    """
    Defines the ability to eticket an entity (Yes, No, Required, Ticketless)
    """
    YES = "Yes"
    NO = "No"
    REQUIRED = "Required"
    TICKETLESS = "Ticketless"
