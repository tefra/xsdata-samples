from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_non_air_reservation_ref_4 import TypeNonAirReservationRef4
from travelport.models.type_segment_ref_4 import TypeSegmentRef4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class ProviderArnksegment3:
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
        namespace = "http://www.travelport.com/schema/common_v33_0"

    previous_segment: None | ProviderArnksegment3.PreviousSegment = field(
        default=None,
        metadata={
            "name": "PreviousSegment",
            "type": "Element",
        }
    )
    next_segment: None | ProviderArnksegment3.NextSegment = field(
        default=None,
        metadata={
            "name": "NextSegment",
            "type": "Element",
        }
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    provider_reservation_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        }
    )

    @dataclass
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
        air_segment_ref: None | TypeSegmentRef4 = field(
            default=None,
            metadata={
                "name": "AirSegmentRef",
                "type": "Element",
            }
        )
        hotel_reservation_ref: None | TypeNonAirReservationRef4 = field(
            default=None,
            metadata={
                "name": "HotelReservationRef",
                "type": "Element",
            }
        )
        vehicle_reservation_ref: None | TypeNonAirReservationRef4 = field(
            default=None,
            metadata={
                "name": "VehicleReservationRef",
                "type": "Element",
            }
        )
        passive_segment_ref: None | TypeSegmentRef4 = field(
            default=None,
            metadata={
                "name": "PassiveSegmentRef",
                "type": "Element",
            }
        )

    @dataclass
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
        air_segment_ref: None | TypeSegmentRef4 = field(
            default=None,
            metadata={
                "name": "AirSegmentRef",
                "type": "Element",
            }
        )
        hotel_reservation_ref: None | TypeNonAirReservationRef4 = field(
            default=None,
            metadata={
                "name": "HotelReservationRef",
                "type": "Element",
            }
        )
        vehicle_reservation_ref: None | TypeNonAirReservationRef4 = field(
            default=None,
            metadata={
                "name": "VehicleReservationRef",
                "type": "Element",
            }
        )
        passive_segment_ref: None | TypeSegmentRef4 = field(
            default=None,
            metadata={
                "name": "PassiveSegmentRef",
                "type": "Element",
            }
        )
