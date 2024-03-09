from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class Maxtype:
    """
    Parameters
    ----------
    hours_max
        Maximum hours. True if unit of time is hours. False if unit of time
        is not hours.
    days_max
        Maximum days. True if unit of time is days. False if unit of time is
        not days.
    months_max
        Maximum months. True if unit of time is months. False if unit of
        time is not months.
    occur_ind_max
        Maximum cccurance indicator. True if day of the week is used. False
        if day of the week is not used.
    same_day_max
        Same day maximum. True if Stay is same day. False if Stay is not
        same day.
    start_ind_max
        Start indicator. True if start indicator. False if not a start
        indicator.
    completion_ind
        Completion indicator. True if Completion C Indicator. False if not
        Completion C Indicator.
    tm_dowmax
        If a max unit of time is true then number corrolates to day of the
        week starting with 1 for Sunday.
    num_occur_max
        Number of maximum occurances.
    """

    class Meta:
        name = "MAXType"

    hours_max: None | bool = field(
        default=None,
        metadata={
            "name": "HoursMax",
            "type": "Attribute",
        },
    )
    days_max: None | bool = field(
        default=None,
        metadata={
            "name": "DaysMax",
            "type": "Attribute",
        },
    )
    months_max: None | bool = field(
        default=None,
        metadata={
            "name": "MonthsMax",
            "type": "Attribute",
        },
    )
    occur_ind_max: None | bool = field(
        default=None,
        metadata={
            "name": "OccurIndMax",
            "type": "Attribute",
        },
    )
    same_day_max: None | bool = field(
        default=None,
        metadata={
            "name": "SameDayMax",
            "type": "Attribute",
        },
    )
    start_ind_max: None | bool = field(
        default=None,
        metadata={
            "name": "StartIndMax",
            "type": "Attribute",
        },
    )
    completion_ind: None | bool = field(
        default=None,
        metadata={
            "name": "CompletionInd",
            "type": "Attribute",
        },
    )
    tm_dowmax: None | int = field(
        default=None,
        metadata={
            "name": "TmDOWMax",
            "type": "Attribute",
        },
    )
    num_occur_max: None | int = field(
        default=None,
        metadata={
            "name": "NumOccurMax",
            "type": "Attribute",
        },
    )
