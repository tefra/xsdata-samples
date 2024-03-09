from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.booking_traveler_name_1 import BookingTravelerName1

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class PnrdivideInfo:
    class Meta:
        name = "PNRDivideInfo"

    booking_traveler_name: list[BookingTravelerName1] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerName",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        },
    )
    provider_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "required": True,
            "max_length": 15,
        },
    )
