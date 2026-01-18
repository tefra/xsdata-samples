from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class TravelDateTimeType:
    """
    Date and time of trip, that allows specifying a time window before and
    after the given date.

    Attributes:
        departure_date_time: This date should be of the form YYYY-MM-
            DDTHH:MM:SS
        arrival_date_time: This date should be of the form YYYY-MM-
            DDTHH:MM:SS
        departure_dates:
        arrival_dates: Allowed only for Advanced Calendar API.
        departure_window: This should be of the form HHMMHHMM.
        arrival_window: This should be of the form HHMMHHMM.
    """

    departure_date_time: None | str = field(
        default=None,
        metadata={
            "name": "DepartureDateTime",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}",
        },
    )
    arrival_date_time: None | str = field(
        default=None,
        metadata={
            "name": "ArrivalDateTime",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}",
        },
    )
    departure_dates: None | TravelDateTimeType.DepartureDates = field(
        default=None,
        metadata={
            "name": "DepartureDates",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    arrival_dates: None | TravelDateTimeType.ArrivalDates = field(
        default=None,
        metadata={
            "name": "ArrivalDates",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    departure_window: None | str = field(
        default=None,
        metadata={
            "name": "DepartureWindow",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "pattern": r"([0-2][0-9][0-5][0-9]){2}",
        },
    )
    arrival_window: None | str = field(
        default=None,
        metadata={
            "name": "ArrivalWindow",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "pattern": r"([0-2][0-9][0-5][0-9]){2}",
        },
    )

    @dataclass(kw_only=True)
    class DepartureDates:
        """
        Attributes:
            day:
            days_range:
            length_of_stay: Amount of days between previous leg's
                DEPARTURE date and current leg's DEPARTURE date. NOTE:
                Allowed only in 2nd or further
                "OriginDestinationInformation". Example: for outbound
                departing on Jan 20, LengthOfStay/@Days="2" means
                inbound departing on Jan 22.
            length_of_stay_range: See comment on "LengthOfStay" element.
        """

        day: list[TravelDateTimeType.DepartureDates.Day] = field(
            default_factory=list,
            metadata={
                "name": "Day",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "sequence": 1,
            },
        )
        days_range: list[TravelDateTimeType.DepartureDates.DaysRange] = field(
            default_factory=list,
            metadata={
                "name": "DaysRange",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "sequence": 1,
            },
        )
        length_of_stay: list[
            TravelDateTimeType.DepartureDates.LengthOfStay
        ] = field(
            default_factory=list,
            metadata={
                "name": "LengthOfStay",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        length_of_stay_range: list[
            TravelDateTimeType.DepartureDates.LengthOfStayRange
        ] = field(
            default_factory=list,
            metadata={
                "name": "LengthOfStayRange",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )

        @dataclass(kw_only=True)
        class LengthOfStay:
            days: int = field(
                metadata={
                    "name": "Days",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass(kw_only=True)
        class LengthOfStayRange:
            """
            Attributes:
                min_days: (inclusive)
                max_days: (inclusive)
            """

            min_days: int = field(
                metadata={
                    "name": "MinDays",
                    "type": "Attribute",
                    "required": True,
                }
            )
            max_days: int = field(
                metadata={
                    "name": "MaxDays",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass(kw_only=True)
        class Day:
            date: str = field(
                metadata={
                    "name": "Date",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}",
                }
            )

        @dataclass(kw_only=True)
        class DaysRange:
            from_date: str = field(
                metadata={
                    "name": "FromDate",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}",
                }
            )
            to_date: str = field(
                metadata={
                    "name": "ToDate",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}",
                }
            )
            week_days: None | str = field(
                default=None,
                metadata={
                    "name": "WeekDays",
                    "type": "Attribute",
                    "pattern": r"[S_][M_][T_][W_][T_][F_][S_]",
                },
            )

    @dataclass(kw_only=True)
    class ArrivalDates:
        day: list[TravelDateTimeType.ArrivalDates.Day] = field(
            default_factory=list,
            metadata={
                "name": "Day",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        days_range: list[TravelDateTimeType.ArrivalDates.DaysRange] = field(
            default_factory=list,
            metadata={
                "name": "DaysRange",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )

        @dataclass(kw_only=True)
        class Day:
            date: str = field(
                metadata={
                    "name": "Date",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}",
                }
            )

        @dataclass(kw_only=True)
        class DaysRange:
            from_date: str = field(
                metadata={
                    "name": "FromDate",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}",
                }
            )
            to_date: str = field(
                metadata={
                    "name": "ToDate",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}",
                }
            )
            week_days: None | str = field(
                default=None,
                metadata={
                    "name": "WeekDays",
                    "type": "Attribute",
                    "pattern": r"[S_][M_][T_][W_][T_][F_][S_]",
                },
            )
