from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass(kw_only=True)
class TypeRemarkWithTravelerRef5:
    """
    Parameters
    ----------
    remark_data
        Actual remarks data.
    booking_traveler_ref
        Reference to Booking Traveler.
    provider_reservation_info_ref
        Provider reservation reference key.
    provider_code
        Contains the Provider Code of the provider for which this element is
        used
    """

    class Meta:
        name = "typeRemarkWithTravelerRef"

    remark_data: str = field(
        metadata={
            "name": "RemarkData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v34_0",
            "required": True,
        }
    )
    booking_traveler_ref: list[str] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v34_0",
            "max_occurs": 999,
        },
    )
    provider_reservation_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        },
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        },
    )
