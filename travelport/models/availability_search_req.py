from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_search_req import AirSearchReq
from travelport.models.point_of_sale_1 import PointOfSale1
from travelport.models.search_passenger_1 import SearchPassenger1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class AvailabilitySearchReq(AirSearchReq):
    """
    Availability Search request.

    Parameters
    ----------
    search_passenger
        Provider: 1G,1V,1P,ACH-Maxinumber of passenger increased in to 18 to
        support 9 INF passenger along with 9 ADT,CHD,INS
        passenger
    point_of_sale
        Provider: ACH.
    return_brand_indicator
        When set to “true”, the Brand Indicator can be returned in the
        availability search response. Provider: 1G, 1V, 1P, ACH
    channel_id
        A Channel ID is 4 alpha-numeric characters used to activate the
        Search Control Console filter for a specific group of travelers
        being served by the agency credential.
    nscc
        Allows the agency to bypass/override the Search Control Console
        rule.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    search_passenger: list[SearchPassenger1] = field(
        default_factory=list,
        metadata={
            "name": "SearchPassenger",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 18,
        },
    )
    point_of_sale: list[PointOfSale1] = field(
        default_factory=list,
        metadata={
            "name": "PointOfSale",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 5,
        },
    )
    return_brand_indicator: bool = field(
        default=False,
        metadata={
            "name": "ReturnBrandIndicator",
            "type": "Attribute",
        },
    )
    channel_id: None | str = field(
        default=None,
        metadata={
            "name": "ChannelId",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 4,
        },
    )
    nscc: None | str = field(
        default=None,
        metadata={
            "name": "NSCC",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 3,
        },
    )
