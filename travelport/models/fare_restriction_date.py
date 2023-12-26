from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.fare_restriction_date_end_date_indicator import (
    FareRestrictionDateEndDateIndicator,
)
from travelport.models.type_fare_directionality import TypeFareDirectionality

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class FareRestrictionDate:
    """Fare restriction based on date ranges.

    StartDate and EndDate are strings representing respective dates. If
    a year component is present then it signifies an exact date. If only
    day and month components are present then it signifies a seasonal
    date, which means applicable for that date in any year

    Parameters
    ----------
    direction
    start_date
    end_date
    end_date_indicator
        This field indicates the end date/last date for which travel on the
        fare component being validated must be commenced or completed
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    direction: None | TypeFareDirectionality = field(
        default=None,
        metadata={
            "name": "Direction",
            "type": "Attribute",
        },
    )
    start_date: None | str = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Attribute",
        },
    )
    end_date: None | str = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Attribute",
        },
    )
    end_date_indicator: None | FareRestrictionDateEndDateIndicator = field(
        default=None,
        metadata={
            "name": "EndDateIndicator",
            "type": "Attribute",
        },
    )
