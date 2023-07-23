from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class Mintype:
    """
    Parameters
    ----------
    hours_min
        Minimum hours. True if unit of time is hours.  False if unit of time
        is not hours.
    days_min
        Minimum days. True if unit of time is days. False if unit of time is
        not days.
    months_min
        Minimum months. True if unit of time is months. False if unit of
        time is not months.
    occur_ind_min
        Minimum occurance indicator. True if day of the week is used. False
        if day of the week is not used.
    same_day_min
        Same day minimum. True if Stay is same day. False if Stay is not
        same day.
    tm_dowmin
        If a min unit of time is true then number corrolates to day of the
        week starting with 1 for Sunday.
    fare_component
        Fare component number of the most restrictive fare.
    num_occur_min
        Number of min occurances. This field is used in conjunction with the
        Day of Week.
    """
    class Meta:
        name = "MINType"

    hours_min: None | bool = field(
        default=None,
        metadata={
            "name": "HoursMin",
            "type": "Attribute",
        }
    )
    days_min: None | bool = field(
        default=None,
        metadata={
            "name": "DaysMin",
            "type": "Attribute",
        }
    )
    months_min: None | bool = field(
        default=None,
        metadata={
            "name": "MonthsMin",
            "type": "Attribute",
        }
    )
    occur_ind_min: None | bool = field(
        default=None,
        metadata={
            "name": "OccurIndMin",
            "type": "Attribute",
        }
    )
    same_day_min: None | bool = field(
        default=None,
        metadata={
            "name": "SameDayMin",
            "type": "Attribute",
        }
    )
    tm_dowmin: None | int = field(
        default=None,
        metadata={
            "name": "TmDOWMin",
            "type": "Attribute",
        }
    )
    fare_component: None | int = field(
        default=None,
        metadata={
            "name": "FareComponent",
            "type": "Attribute",
        }
    )
    num_occur_min: None | int = field(
        default=None,
        metadata={
            "name": "NumOccurMin",
            "type": "Attribute",
        }
    )
