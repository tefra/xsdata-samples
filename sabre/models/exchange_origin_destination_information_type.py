from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.cabin_pref_type import CabinPrefType
from sabre.models.exchange_origin_destination_flight_type import (
    ExchangeOriginDestinationFlightType,
)
from sabre.models.origin_destination_information_type import (
    OriginDestinationInformationType,
)
from sabre.models.request_location_type import RequestLocationType
from sabre.models.segment_type_code import SegmentTypeCode

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class ExchangeOriginDestinationInformationType(
    OriginDestinationInformationType
):
    """
    Attributes:
        flight:
        date_flexibility: The number of alternate days around the travel
            date to search.
        sister_destination_location: List of alternate destination
            cities to search
        sister_destination_mileage:
        sister_origin_location: List of alternate origin cities to
            search
        sister_origin_mileage:
        segment_type:
        alternate_time: Maximum time difference/deviation allowed.
        max_one_way_options: Maximum number of options to return.
        num_one_way_options: Number of options for requested date.
        cabin_pref: Defines preferred cabin to be used in a search for
            this leg level (if SegmentType is "O") or segment (if
            SegmentType is "X"). The cabin type specified in this
            element will override the cabin type specified at the
            request level for this leg/segment. If a cabin type is not
            specified for this element the cabin type at request level
            will be used as default for this leg or segment. If the
            cabin type is not specified at both the leg/segment level
            and request level a default cabin of "Economy" will be used?
        connection_time: Connection time between segments.
        total_travel_time: Total travel time settings
    """

    flight: list[ExchangeOriginDestinationFlightType] = field(
        default_factory=list,
        metadata={
            "name": "Flight",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_occurs": 1,
        },
    )
    date_flexibility: list[
        ExchangeOriginDestinationInformationType.DateFlexibility
    ] = field(
        default_factory=list,
        metadata={
            "name": "DateFlexibility",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 2,
        },
    )
    sister_destination_location: list[RequestLocationType] = field(
        default_factory=list,
        metadata={
            "name": "SisterDestinationLocation",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    sister_destination_mileage: (
        None
        | ExchangeOriginDestinationInformationType.SisterDestinationMileage
    ) = field(
        default=None,
        metadata={
            "name": "SisterDestinationMileage",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    sister_origin_location: list[RequestLocationType] = field(
        default_factory=list,
        metadata={
            "name": "SisterOriginLocation",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    sister_origin_mileage: (
        None | ExchangeOriginDestinationInformationType.SisterOriginMileage
    ) = field(
        default=None,
        metadata={
            "name": "SisterOriginMileage",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    segment_type: (
        None | ExchangeOriginDestinationInformationType.SegmentType
    ) = field(
        default=None,
        metadata={
            "name": "SegmentType",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    alternate_time: (
        None | ExchangeOriginDestinationInformationType.AlternateTime
    ) = field(
        default=None,
        metadata={
            "name": "AlternateTime",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    max_one_way_options: (
        None | ExchangeOriginDestinationInformationType.MaxOneWayOptions
    ) = field(
        default=None,
        metadata={
            "name": "MaxOneWayOptions",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    num_one_way_options: (
        None | ExchangeOriginDestinationInformationType.NumOneWayOptions
    ) = field(
        default=None,
        metadata={
            "name": "NumOneWayOptions",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    cabin_pref: None | CabinPrefType = field(
        default=None,
        metadata={
            "name": "CabinPref",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    connection_time: (
        None | ExchangeOriginDestinationInformationType.ConnectionTime
    ) = field(
        default=None,
        metadata={
            "name": "ConnectionTime",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    total_travel_time: (
        None | ExchangeOriginDestinationInformationType.TotalTravelTime
    ) = field(
        default=None,
        metadata={
            "name": "TotalTravelTime",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )

    @dataclass(kw_only=True)
    class DateFlexibility:
        """
        Attributes:
            nbr_of_days: Number of alternate dates before and after
                requested travel date.
            plus: Number of alternate dates before requested travel
                date.
            minus: Number of alternate dates after requested travel
                date.
            validate_value: Flag telling if dates within the specified
                range should be processed in the validate path.
        """

        nbr_of_days: None | int = field(
            default=None,
            metadata={
                "name": "NbrOfDays",
                "type": "Attribute",
            },
        )
        plus: None | int = field(
            default=None,
            metadata={
                "name": "Plus",
                "type": "Attribute",
            },
        )
        minus: None | int = field(
            default=None,
            metadata={
                "name": "Minus",
                "type": "Attribute",
            },
        )
        validate_value: None | bool = field(
            default=None,
            metadata={
                "name": "Validate",
                "type": "Attribute",
            },
        )

    @dataclass(kw_only=True)
    class SisterDestinationMileage:
        number: int = field(
            metadata={
                "name": "Number",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class SisterOriginMileage:
        number: int = field(
            metadata={
                "name": "Number",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class SegmentType:
        """
        Attributes:
            code: "Code" can be "ARUNK", "O" for normal, or "X" for
                connection.
        """

        code: None | SegmentTypeCode = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            },
        )

    @dataclass(kw_only=True)
    class AlternateTime:
        """
        Attributes:
            plus_minus: Maximum time difference between actual and
                desired time.
            plus: Maximum number of hours after desired time.
            minus: Maximum number of hours before desired time.
        """

        plus_minus: None | int = field(
            default=None,
            metadata={
                "name": "PlusMinus",
                "type": "Attribute",
                "min_inclusive": 0,
                "max_inclusive": 9,
            },
        )
        plus: None | int = field(
            default=None,
            metadata={
                "name": "Plus",
                "type": "Attribute",
                "min_inclusive": 0,
                "max_inclusive": 9,
            },
        )
        minus: None | int = field(
            default=None,
            metadata={
                "name": "Minus",
                "type": "Attribute",
                "min_inclusive": 0,
                "max_inclusive": 72,
            },
        )

    @dataclass(kw_only=True)
    class MaxOneWayOptions:
        value: int = field(
            metadata={
                "name": "Value",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class NumOneWayOptions:
        number: int = field(
            metadata={
                "name": "Number",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ConnectionTime:
        """
        Attributes:
            min:
            max:
            excluded_connection_begin: Excluded connection time begin in
                format HHMM
            excluded_connection_end: Excluded connection time end in
                format HHMM
            enable_excluded_connection: Enable excluded connection time
                (default: true)
        """

        min: None | int = field(
            default=None,
            metadata={
                "name": "Min",
                "type": "Attribute",
            },
        )
        max: None | int = field(
            default=None,
            metadata={
                "name": "Max",
                "type": "Attribute",
            },
        )
        excluded_connection_begin: None | str = field(
            default=None,
            metadata={
                "name": "ExcludedConnectionBegin",
                "type": "Attribute",
                "pattern": r"([0-1][0-9]|2[0-3])[0-5][0-9]",
            },
        )
        excluded_connection_end: None | str = field(
            default=None,
            metadata={
                "name": "ExcludedConnectionEnd",
                "type": "Attribute",
                "pattern": r"([0-1][0-9]|2[0-3])[0-5][0-9]",
            },
        )
        enable_excluded_connection: None | bool = field(
            default=None,
            metadata={
                "name": "EnableExcludedConnection",
                "type": "Attribute",
            },
        )

    @dataclass(kw_only=True)
    class TotalTravelTime:
        min: None | int = field(
            default=None,
            metadata={
                "name": "Min",
                "type": "Attribute",
            },
        )
        max: None | int = field(
            default=None,
            metadata={
                "name": "Max",
                "type": "Attribute",
            },
        )
