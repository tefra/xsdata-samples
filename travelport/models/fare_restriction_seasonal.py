from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class FareRestrictionSeasonal:
    """
    Fares Restricted based on the season requested.

    StartDate and EndDate are strings representing respective dates. If a
    year component is present then it signifies an exact date. If only day
    and month components are present then it signifies a seasonal date,
    which means applicable for that date in any year.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    comment: None | str = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Attribute",
        },
    )
    variation_by_travel_dates: None | str = field(
        default=None,
        metadata={
            "name": "VariationByTravelDates",
            "type": "Attribute",
        },
    )
    seasonal_range1_ind: None | str = field(
        default=None,
        metadata={
            "name": "SeasonalRange1Ind",
            "type": "Attribute",
        },
    )
    seasonal_range1_start_date: None | str = field(
        default=None,
        metadata={
            "name": "SeasonalRange1StartDate",
            "type": "Attribute",
        },
    )
    seasonal_range1_end_date: None | str = field(
        default=None,
        metadata={
            "name": "SeasonalRange1EndDate",
            "type": "Attribute",
        },
    )
    seasonal_range2_ind: None | str = field(
        default=None,
        metadata={
            "name": "SeasonalRange2Ind",
            "type": "Attribute",
        },
    )
    seasonal_range2_start_date: None | str = field(
        default=None,
        metadata={
            "name": "SeasonalRange2StartDate",
            "type": "Attribute",
        },
    )
    seasonal_range2_end_date: None | str = field(
        default=None,
        metadata={
            "name": "SeasonalRange2EndDate",
            "type": "Attribute",
        },
    )
