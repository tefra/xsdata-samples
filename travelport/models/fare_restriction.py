from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.fare_restriction_date import FareRestrictionDate
from travelport.models.fare_restriction_days_of_week import (
    FareRestrictionDaysOfWeek,
)
from travelport.models.fare_restriction_sale_date import (
    FareRestrictionSaleDate,
)
from travelport.models.fare_restriction_seasonal import FareRestrictionSeasonal
from travelport.models.type_fare_restriction_type import (
    TypeFareRestrictionType,
)

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class FareRestriction:
    """
    Fare Restriction.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    fare_restriction_days_of_week: list[FareRestrictionDaysOfWeek] = field(
        default_factory=list,
        metadata={
            "name": "FareRestrictionDaysOfWeek",
            "type": "Element",
            "max_occurs": 3,
        },
    )
    fare_restriction_date: list[FareRestrictionDate] = field(
        default_factory=list,
        metadata={
            "name": "FareRestrictionDate",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    fare_restriction_sale_date: None | FareRestrictionSaleDate = field(
        default=None,
        metadata={
            "name": "FareRestrictionSaleDate",
            "type": "Element",
        },
    )
    fare_restriction_seasonal: list[FareRestrictionSeasonal] = field(
        default_factory=list,
        metadata={
            "name": "FareRestrictionSeasonal",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    fare_restrictiontype: None | TypeFareRestrictionType = field(
        default=None,
        metadata={
            "name": "FareRestrictiontype",
            "type": "Attribute",
        },
    )
