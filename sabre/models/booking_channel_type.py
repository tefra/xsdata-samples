from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class BookingChannelType:
    """
    Specifies the booking channel types and whether it is the primary means of
    connectivity of the source.

    Attributes:
        type_value: The type of booking channel (e.g. Global
            Distribution System (GDS), Alternative Distribution System
            (ADS), Sales and Catering System (SCS), Property Management
            System (PMS), Central Reservation System (CRS), Tour
            Operator System (TOS), Internet and ALL). Refer to OTA Code
            List Booking Channel Type (BCT).
        primary: Indicates whether the enumerated booking channel is the
            primary means of connectivity used by the source.
    """

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
    primary: None | bool = field(
        default=None,
        metadata={
            "name": "Primary",
            "type": "Attribute",
        },
    )
