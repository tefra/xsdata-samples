from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_search_modifiers_order_by import (
    AirSearchModifiersOrderBy,
)
from travelport.models.alliance import Alliance
from travelport.models.booking_code import BookingCode
from travelport.models.carrier_1 import Carrier1
from travelport.models.flight_type import FlightType
from travelport.models.max_layover_duration_type import MaxLayoverDurationType
from travelport.models.permitted_cabins import PermittedCabins
from travelport.models.permitted_carriers import PermittedCarriers
from travelport.models.preferred_booking_codes import PreferredBookingCodes
from travelport.models.preferred_cabins import PreferredCabins
from travelport.models.preferred_carriers import PreferredCarriers
from travelport.models.prohibited_carriers import ProhibitedCarriers
from travelport.models.provider_1 import Provider1
from travelport.models.type_distance import TypeDistance
from travelport.models.type_native_search_modifier import (
    TypeNativeSearchModifier,
)

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class AirSearchModifiers:
    """
    Controls and switches for the Air Search request.

    Parameters
    ----------
    disfavored_providers
    preferred_providers
    disfavored_carriers
    permitted_carriers
    prohibited_carriers
    preferred_carriers
    permitted_cabins
    preferred_cabins
    preferred_alliances
    disfavored_alliances
    permitted_booking_codes
        This is the container to specify all permitted booking codes
    preferred_booking_codes
    prohibited_booking_codes
        This is the container to specify all prohibited booking codes
    flight_type
    max_layover_duration
        This is the maximum duration the layover may have for each trip in
        the request. Supported providers 1P.
    native_search_modifier
        Container for Native command modifiers. Providers supported : 1P
    distance_type
    include_flight_details
    allow_change_of_airport
    prohibit_overnight_layovers
        If true, excludes connections if arrival time of first flight and
        departure time of second flight is on 2 different calendar days.
        When used in conjunction with MaxConnectionTime, it would exclude
        all connections if the connecting flights wait time exceeds the time
        specified in MaxConnectionTime.
    max_solutions
        The maximum number of solutions to return. Decreasing this number
    max_connection_time
        The maximum anount of time (in minutes) that a solution can contain
        for connections between flights.
    search_weekends
        A value of true indicates that search should be expanded to include
        weekend combinations, if applicable.
    include_extra_solutions
        If true, indicates that search should be made for returning more
        solutions, if available. For example, for certain providers, premium
        members may have the facility to get more solutions. This attribute
        may have to be combined with other applicable modifiers (like
        SearchWeekends) to return more results.
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
        Arrival Time. Applicable to air availability only.
    exclude_open_jaw_airport
        This option ensures that travel into/out of each location will be
        into/out of the same airport of that location. Values are true or
        false. Default value is 'false'. If value is true then open jaws are
        exclude. If false the open jaws are included. The supported
        providers: 1P
    exclude_ground_transportation
        Indicates whether to allow the user to exclude ground transportation
        or not. Default value is 'false'. If value is true then ground
        transportations are excluded. If false then ground transportations
        are included. The supported providers: 1P
    max_journey_time
        Maximum Journey Time for all legs (in hours) 0-99. For LFS Supported
        Providers are 1G,1V,1P. For AirAvail Supported Providers are 1G,1V.
    jet_service_only
        Restricts results to Jet service flights only.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    disfavored_providers: None | AirSearchModifiers.DisfavoredProviders = (
        field(
            default=None,
            metadata={
                "name": "DisfavoredProviders",
                "type": "Element",
            },
        )
    )
    preferred_providers: None | AirSearchModifiers.PreferredProviders = field(
        default=None,
        metadata={
            "name": "PreferredProviders",
            "type": "Element",
        },
    )
    disfavored_carriers: None | AirSearchModifiers.DisfavoredCarriers = field(
        default=None,
        metadata={
            "name": "DisfavoredCarriers",
            "type": "Element",
        },
    )
    permitted_carriers: None | PermittedCarriers = field(
        default=None,
        metadata={
            "name": "PermittedCarriers",
            "type": "Element",
        },
    )
    prohibited_carriers: None | ProhibitedCarriers = field(
        default=None,
        metadata={
            "name": "ProhibitedCarriers",
            "type": "Element",
        },
    )
    preferred_carriers: None | PreferredCarriers = field(
        default=None,
        metadata={
            "name": "PreferredCarriers",
            "type": "Element",
        },
    )
    permitted_cabins: None | PermittedCabins = field(
        default=None,
        metadata={
            "name": "PermittedCabins",
            "type": "Element",
        },
    )
    preferred_cabins: None | PreferredCabins = field(
        default=None,
        metadata={
            "name": "PreferredCabins",
            "type": "Element",
        },
    )
    preferred_alliances: None | AirSearchModifiers.PreferredAlliances = field(
        default=None,
        metadata={
            "name": "PreferredAlliances",
            "type": "Element",
        },
    )
    disfavored_alliances: None | AirSearchModifiers.DisfavoredAlliances = (
        field(
            default=None,
            metadata={
                "name": "DisfavoredAlliances",
                "type": "Element",
            },
        )
    )
    permitted_booking_codes: (
        None | AirSearchModifiers.PermittedBookingCodes
    ) = field(
        default=None,
        metadata={
            "name": "PermittedBookingCodes",
            "type": "Element",
        },
    )
    preferred_booking_codes: None | PreferredBookingCodes = field(
        default=None,
        metadata={
            "name": "PreferredBookingCodes",
            "type": "Element",
        },
    )
    prohibited_booking_codes: (
        None | AirSearchModifiers.ProhibitedBookingCodes
    ) = field(
        default=None,
        metadata={
            "name": "ProhibitedBookingCodes",
            "type": "Element",
        },
    )
    flight_type: None | FlightType = field(
        default=None,
        metadata={
            "name": "FlightType",
            "type": "Element",
        },
    )
    max_layover_duration: None | MaxLayoverDurationType = field(
        default=None,
        metadata={
            "name": "MaxLayoverDuration",
            "type": "Element",
        },
    )
    native_search_modifier: None | TypeNativeSearchModifier = field(
        default=None,
        metadata={
            "name": "NativeSearchModifier",
            "type": "Element",
        },
    )
    distance_type: TypeDistance = field(
        default=TypeDistance.MI,
        metadata={
            "name": "DistanceType",
            "type": "Attribute",
        },
    )
    include_flight_details: bool = field(
        default=True,
        metadata={
            "name": "IncludeFlightDetails",
            "type": "Attribute",
        },
    )
    allow_change_of_airport: bool = field(
        default=True,
        metadata={
            "name": "AllowChangeOfAirport",
            "type": "Attribute",
        },
    )
    prohibit_overnight_layovers: bool = field(
        default=False,
        metadata={
            "name": "ProhibitOvernightLayovers",
            "type": "Attribute",
        },
    )
    max_solutions: None | int = field(
        default=None,
        metadata={
            "name": "MaxSolutions",
            "type": "Attribute",
        },
    )
    max_connection_time: None | int = field(
        default=None,
        metadata={
            "name": "MaxConnectionTime",
            "type": "Attribute",
        },
    )
    search_weekends: None | bool = field(
        default=None,
        metadata={
            "name": "SearchWeekends",
            "type": "Attribute",
        },
    )
    include_extra_solutions: None | bool = field(
        default=None,
        metadata={
            "name": "IncludeExtraSolutions",
            "type": "Attribute",
        },
    )
    prohibit_multi_airport_connection: None | bool = field(
        default=None,
        metadata={
            "name": "ProhibitMultiAirportConnection",
            "type": "Attribute",
        },
    )
    prefer_non_stop: bool = field(
        default=False,
        metadata={
            "name": "PreferNonStop",
            "type": "Attribute",
        },
    )
    order_by: None | AirSearchModifiersOrderBy = field(
        default=None,
        metadata={
            "name": "OrderBy",
            "type": "Attribute",
        },
    )
    exclude_open_jaw_airport: bool = field(
        default=False,
        metadata={
            "name": "ExcludeOpenJawAirport",
            "type": "Attribute",
        },
    )
    exclude_ground_transportation: bool = field(
        default=False,
        metadata={
            "name": "ExcludeGroundTransportation",
            "type": "Attribute",
        },
    )
    max_journey_time: None | int = field(
        default=None,
        metadata={
            "name": "MaxJourneyTime",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 99,
        },
    )
    jet_service_only: None | bool = field(
        default=None,
        metadata={
            "name": "JetServiceOnly",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class DisfavoredProviders:
        provider: list[Provider1] = field(
            default_factory=list,
            metadata={
                "name": "Provider",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
                "min_occurs": 1,
                "max_occurs": 999,
            },
        )

    @dataclass(kw_only=True)
    class PreferredProviders:
        provider: list[Provider1] = field(
            default_factory=list,
            metadata={
                "name": "Provider",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
                "min_occurs": 1,
                "max_occurs": 999,
            },
        )

    @dataclass(kw_only=True)
    class DisfavoredCarriers:
        carrier: list[Carrier1] = field(
            default_factory=list,
            metadata={
                "name": "Carrier",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
                "min_occurs": 1,
                "max_occurs": 999,
            },
        )

    @dataclass(kw_only=True)
    class PreferredAlliances:
        alliance: list[Alliance] = field(
            default_factory=list,
            metadata={
                "name": "Alliance",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            },
        )

    @dataclass(kw_only=True)
    class DisfavoredAlliances:
        alliance: list[Alliance] = field(
            default_factory=list,
            metadata={
                "name": "Alliance",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            },
        )

    @dataclass(kw_only=True)
    class PermittedBookingCodes:
        booking_code: list[BookingCode] = field(
            default_factory=list,
            metadata={
                "name": "BookingCode",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            },
        )

    @dataclass(kw_only=True)
    class ProhibitedBookingCodes:
        booking_code: list[BookingCode] = field(
            default_factory=list,
            metadata={
                "name": "BookingCode",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            },
        )
