from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_leg_modifiers_order_by import AirLegModifiersOrderBy
from travelport.models.alliance import Alliance
from travelport.models.booking_code import BookingCode
from travelport.models.connection_point_1 import ConnectionPoint1
from travelport.models.flight_type import FlightType
from travelport.models.permitted_cabins import PermittedCabins
from travelport.models.permitted_carriers import PermittedCarriers
from travelport.models.preferred_booking_codes import PreferredBookingCodes
from travelport.models.preferred_cabins import PreferredCabins
from travelport.models.preferred_carriers import PreferredCarriers
from travelport.models.prohibited_carriers import ProhibitedCarriers
from travelport.models.type_anchor_flight_data import TypeAnchorFlightData

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirLegModifiers:
    """
    Parameters
    ----------
    permitted_cabins
    preferred_cabins
    permitted_carriers
    prohibited_carriers
    preferred_carriers
    permitted_connection_points
        This is the container to specify all permitted connection points.
        Applicable for 1G/1V/1P.
    prohibited_connection_points
        This is the container to specify all prohibited connection points.
        Applicable for 1G/1V/1P.
    preferred_connection_points
        This is the container to specify all preferred connection points.
        Applicable for 1G/1V only.
    permitted_booking_codes
        This is the container to specify all permitted booking codes
    preferred_booking_codes
    preferred_alliances
    prohibited_booking_codes
        This is the container to specify all prohibited booking codes
    disfavored_alliances
    flight_type
    anchor_flight_data
    prohibit_overnight_layovers
        If true, excludes connections if arrival time of first flight and
        departure time of second flight is on 2 different calendar days.
        When used in conjunction with MaxConnectionTime, it would exclude
        all connections if the connecting flights wait time exceeds the time
        specified in MaxConnectionTime.
    max_connection_time
    return_first_available_only
        If it is true then it will search for first available for the
        booking code designated or any booking code in same cabin.
    allow_direct_access
        If it is true request will be sent directly to the carrier.
    prohibit_multi_airport_connection
        Indicates whether to restrict multi-airport connections
    prefer_non_stop
        When non-stops are preferred, the distribution of search results
        should skew heavily toward non-stop flights while still returning
        some one stop flights for comparison and price competitiveness. The
        search request will ‘boost' the preference towards non-stops. If
        true then Non Stop flights will be preferred.
    order_by
        Indicates whether to sort by Journey Time, Deparature Time or
        Arrival Time
    max_journey_time
        Maximum Journey Time for this leg (in hours) 0-99. Supported
        Providers 1G,1V.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    permitted_cabins: None | PermittedCabins = field(
        default=None,
        metadata={
            "name": "PermittedCabins",
            "type": "Element",
        }
    )
    preferred_cabins: None | PreferredCabins = field(
        default=None,
        metadata={
            "name": "PreferredCabins",
            "type": "Element",
        }
    )
    permitted_carriers: None | PermittedCarriers = field(
        default=None,
        metadata={
            "name": "PermittedCarriers",
            "type": "Element",
        }
    )
    prohibited_carriers: None | ProhibitedCarriers = field(
        default=None,
        metadata={
            "name": "ProhibitedCarriers",
            "type": "Element",
        }
    )
    preferred_carriers: None | PreferredCarriers = field(
        default=None,
        metadata={
            "name": "PreferredCarriers",
            "type": "Element",
        }
    )
    permitted_connection_points: None | AirLegModifiers.PermittedConnectionPoints = field(
        default=None,
        metadata={
            "name": "PermittedConnectionPoints",
            "type": "Element",
        }
    )
    prohibited_connection_points: None | AirLegModifiers.ProhibitedConnectionPoints = field(
        default=None,
        metadata={
            "name": "ProhibitedConnectionPoints",
            "type": "Element",
        }
    )
    preferred_connection_points: None | AirLegModifiers.PreferredConnectionPoints = field(
        default=None,
        metadata={
            "name": "PreferredConnectionPoints",
            "type": "Element",
        }
    )
    permitted_booking_codes: None | AirLegModifiers.PermittedBookingCodes = field(
        default=None,
        metadata={
            "name": "PermittedBookingCodes",
            "type": "Element",
        }
    )
    preferred_booking_codes: None | PreferredBookingCodes = field(
        default=None,
        metadata={
            "name": "PreferredBookingCodes",
            "type": "Element",
        }
    )
    preferred_alliances: None | AirLegModifiers.PreferredAlliances = field(
        default=None,
        metadata={
            "name": "PreferredAlliances",
            "type": "Element",
        }
    )
    prohibited_booking_codes: None | AirLegModifiers.ProhibitedBookingCodes = field(
        default=None,
        metadata={
            "name": "ProhibitedBookingCodes",
            "type": "Element",
        }
    )
    disfavored_alliances: None | AirLegModifiers.DisfavoredAlliances = field(
        default=None,
        metadata={
            "name": "DisfavoredAlliances",
            "type": "Element",
        }
    )
    flight_type: None | FlightType = field(
        default=None,
        metadata={
            "name": "FlightType",
            "type": "Element",
        }
    )
    anchor_flight_data: None | TypeAnchorFlightData = field(
        default=None,
        metadata={
            "name": "AnchorFlightData",
            "type": "Element",
        }
    )
    prohibit_overnight_layovers: bool = field(
        default=False,
        metadata={
            "name": "ProhibitOvernightLayovers",
            "type": "Attribute",
        }
    )
    max_connection_time: None | int = field(
        default=None,
        metadata={
            "name": "MaxConnectionTime",
            "type": "Attribute",
        }
    )
    return_first_available_only: None | bool = field(
        default=None,
        metadata={
            "name": "ReturnFirstAvailableOnly",
            "type": "Attribute",
        }
    )
    allow_direct_access: bool = field(
        default=False,
        metadata={
            "name": "AllowDirectAccess",
            "type": "Attribute",
        }
    )
    prohibit_multi_airport_connection: None | bool = field(
        default=None,
        metadata={
            "name": "ProhibitMultiAirportConnection",
            "type": "Attribute",
        }
    )
    prefer_non_stop: bool = field(
        default=False,
        metadata={
            "name": "PreferNonStop",
            "type": "Attribute",
        }
    )
    order_by: None | AirLegModifiersOrderBy = field(
        default=None,
        metadata={
            "name": "OrderBy",
            "type": "Attribute",
        }
    )
    max_journey_time: None | int = field(
        default=None,
        metadata={
            "name": "MaxJourneyTime",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 99,
        }
    )

    @dataclass
    class PermittedConnectionPoints:
        connection_point: list[ConnectionPoint1] = field(
            default_factory=list,
            metadata={
                "name": "ConnectionPoint",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )

    @dataclass
    class ProhibitedConnectionPoints:
        connection_point: list[ConnectionPoint1] = field(
            default_factory=list,
            metadata={
                "name": "ConnectionPoint",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )

    @dataclass
    class PreferredConnectionPoints:
        connection_point: list[ConnectionPoint1] = field(
            default_factory=list,
            metadata={
                "name": "ConnectionPoint",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
                "min_occurs": 1,
                "max_occurs": 99,
            }
        )

    @dataclass
    class PermittedBookingCodes:
        booking_code: list[BookingCode] = field(
            default_factory=list,
            metadata={
                "name": "BookingCode",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )

    @dataclass
    class PreferredAlliances:
        alliance: list[Alliance] = field(
            default_factory=list,
            metadata={
                "name": "Alliance",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )

    @dataclass
    class ProhibitedBookingCodes:
        booking_code: list[BookingCode] = field(
            default_factory=list,
            metadata={
                "name": "BookingCode",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )

    @dataclass
    class DisfavoredAlliances:
        alliance: list[Alliance] = field(
            default_factory=list,
            metadata={
                "name": "Alliance",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            }
        )
