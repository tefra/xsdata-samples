from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_price_point import AirPricePoint

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirPricePointList:
    """
    Provides the list of AirPricePoint (Non Solutioned Result).

    Parameters
    ----------
    air_price_point
        The container which holds the Non Solutioned result. Different
        options for each search leg requested will be returned and one
        option for each search leg can be selected.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_price_point: list[AirPricePoint] = field(
        default_factory=list,
        metadata={
            "name": "AirPricePoint",
            "type": "Element",
            "max_occurs": 999,
        },
    )
