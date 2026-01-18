from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.account_code_1 import AccountCode1
from travelport.models.air_itinerary_details import AirItineraryDetails

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class MerchandisingDetails:
    """
    Rich Content and Branding for a fare brand.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_itinerary_details: list[AirItineraryDetails] = field(
        default_factory=list,
        metadata={
            "name": "AirItineraryDetails",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 99,
        },
    )
    account_code: list[AccountCode1] = field(
        default_factory=list,
        metadata={
            "name": "AccountCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 10,
        },
    )
