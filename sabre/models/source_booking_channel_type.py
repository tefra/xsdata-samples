from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.booking_channel_type import BookingChannelType
from sabre.models.company_name_type import CompanyNameType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class SourceBookingChannelType(BookingChannelType):
    """
    Specifies the booking channel type and whether it is the primary means
    of connectivity of the source.

    Attributes:
        company_name: Identifies the company that is associated with the
            booking channel.
    """

    company_name: None | CompanyNameType = field(
        default=None,
        metadata={
            "name": "CompanyName",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
