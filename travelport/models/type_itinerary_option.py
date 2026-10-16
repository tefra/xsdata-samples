from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeItineraryOption(StrEnum):
    NO_FARE = "NoFare"
    NO_AMOUNT = "NoAmount"
    SEQUENCE_NUMBER = "SequenceNumber"
