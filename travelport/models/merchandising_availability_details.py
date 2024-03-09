from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.account_code_1 import AccountCode1
from travelport.models.air_itinerary_details import AirItineraryDetails

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class MerchandisingAvailabilityDetails:
    """
    Rich Content and Branding for an air segment.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_itinerary_details: None | AirItineraryDetails = field(
        default=None,
        metadata={
            "name": "AirItineraryDetails",
            "type": "Element",
            "required": True,
        },
    )
    account_code: None | AccountCode1 = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
