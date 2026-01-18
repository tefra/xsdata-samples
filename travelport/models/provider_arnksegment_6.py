from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_non_air_reservation_ref_7 import (
    TypeNonAirReservationRef7,
)
from travelport.models.type_segment_ref_7 import TypeSegmentRef7

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass(kw_only=True)
class ProviderArnksegment6:
    """
    Represents host ARNK segments.

    Parameters
    ----------
    previous_segment
    next_segment
    key
    provider_reservation_info_ref
        Provider reservation reference key.
    """

    class Meta:
        name = "ProviderARNKSegment"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    previous_segment: None | ProviderArnksegment6.PreviousSegment = field(
        default=None,
        metadata={
            "name": "PreviousSegment",
            "type": "Element",
        },
    )
    next_segment: None | ProviderArnksegment6.NextSegment = field(
        default=None,
        metadata={
            "name": "NextSegment",
            "type": "Element",
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    provider_reservation_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class PreviousSegment:
        """
        Parameters
        ----------
        air_segment_ref
            Reference to AirSegment from an Air Reservation.
        hotel_reservation_ref
            Specify the locator code of Hotel reservation.
        vehicle_reservation_ref
            Specify the locator code of Vehicle reservation.
        passive_segment_ref
            Reference to PassiveSegment from a Passive Reservation.
        """

        air_segment_ref: None | TypeSegmentRef7 = field(
            default=None,
            metadata={
                "name": "AirSegmentRef",
                "type": "Element",
            },
        )
        hotel_reservation_ref: None | TypeNonAirReservationRef7 = field(
            default=None,
            metadata={
                "name": "HotelReservationRef",
                "type": "Element",
            },
        )
        vehicle_reservation_ref: None | TypeNonAirReservationRef7 = field(
            default=None,
            metadata={
                "name": "VehicleReservationRef",
                "type": "Element",
            },
        )
        passive_segment_ref: None | TypeSegmentRef7 = field(
            default=None,
            metadata={
                "name": "PassiveSegmentRef",
                "type": "Element",
            },
        )

    @dataclass(kw_only=True)
    class NextSegment:
        """
        Parameters
        ----------
        air_segment_ref
            Reference to AirSegment from an Air Reservation.
        hotel_reservation_ref
            Specify the locator code of Hotel reservation.
        vehicle_reservation_ref
            Specify the locator code of Vehicle reservation.
        passive_segment_ref
            Reference to PassiveSegment from a Passive Reservation.
        """

        air_segment_ref: None | TypeSegmentRef7 = field(
            default=None,
            metadata={
                "name": "AirSegmentRef",
                "type": "Element",
            },
        )
        hotel_reservation_ref: None | TypeNonAirReservationRef7 = field(
            default=None,
            metadata={
                "name": "HotelReservationRef",
                "type": "Element",
            },
        )
        vehicle_reservation_ref: None | TypeNonAirReservationRef7 = field(
            default=None,
            metadata={
                "name": "VehicleReservationRef",
                "type": "Element",
            },
        )
        passive_segment_ref: None | TypeSegmentRef7 = field(
            default=None,
            metadata={
                "name": "PassiveSegmentRef",
                "type": "Element",
            },
        )
