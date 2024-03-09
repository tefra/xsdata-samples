from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class TypeFormOfPaymentPnrreference3:
    """
    Parameters
    ----------
    key
        Unique ID to identify a ProviderReservationInfo
    provider_reservation_level
        It means that the form of payment is applied at ProviderReservation
        level.
    """

    class Meta:
        name = "typeFormOfPaymentPNRReference"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    provider_reservation_level: bool = field(
        default=True,
        metadata={
            "name": "ProviderReservationLevel",
            "type": "Attribute",
        },
    )
