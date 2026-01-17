from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class CustomerReceiptInfo:
    """
    Information about customer receipt via email.

    Supported providers are 1V/1G/1P.

    Parameters
    ----------
    booking_traveler_ref
        Refererence of the Booking Traveler related to the email.
    email_ref
        Reference to the email address used for receipt of EMD.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    booking_traveler_ref: None | str = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
            "required": True,
        },
    )
    email_ref: None | str = field(
        default=None,
        metadata={
            "name": "EmailRef",
            "type": "Attribute",
            "required": True,
        },
    )
