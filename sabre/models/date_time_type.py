from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class DateTimeType:
    """
    Attributes:
        time_window_start: Allowed amount of time before specified time.
        time_window_end: Allowed amount of time after specified time.
        time_tolerance: Maximum time difference between actual and
            desired time.
        date_flexibility: The number of alternate days around the travel
            date to search.
        max_options_per_date: Number of options for requested date.
        connection_time_min: Minimal amount of time between flights
        connection_time_max: Maximal amount of time between flights
    """

    time_window_start: None | str = field(
        default=None,
        metadata={
            "name": "TimeWindowStart",
            "type": "Attribute",
            "pattern": r"([0-1][0-9]|2[0-3])[0-5][0-9]",
        },
    )
    time_window_end: None | str = field(
        default=None,
        metadata={
            "name": "TimeWindowEnd",
            "type": "Attribute",
            "pattern": r"([0-1][0-9]|2[0-3])[0-5][0-9]",
        },
    )
    time_tolerance: None | int = field(
        default=None,
        metadata={
            "name": "TimeTolerance",
            "type": "Attribute",
        },
    )
    date_flexibility: None | int = field(
        default=None,
        metadata={
            "name": "DateFlexibility",
            "type": "Attribute",
        },
    )
    max_options_per_date: None | int = field(
        default=None,
        metadata={
            "name": "MaxOptionsPerDate",
            "type": "Attribute",
        },
    )
    connection_time_min: None | int = field(
        default=None,
        metadata={
            "name": "ConnectionTimeMin",
            "type": "Attribute",
        },
    )
    connection_time_max: None | int = field(
        default=None,
        metadata={
            "name": "ConnectionTimeMax",
            "type": "Attribute",
        },
    )
