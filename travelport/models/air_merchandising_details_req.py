from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_1 import BaseReq1
from travelport.models.merchandising_availability_details import (
    MerchandisingAvailabilityDetails,
)
from travelport.models.merchandising_details import MerchandisingDetails
from travelport.models.optional_service_modifiers import (
    OptionalServiceModifiers,
)

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class AirMerchandisingDetailsReq(BaseReq1):
    """
    Request to retrieve brand details and optional services included in the
    brand.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    merchandising_details: None | MerchandisingDetails = field(
        default=None,
        metadata={
            "name": "MerchandisingDetails",
            "type": "Element",
        },
    )
    optional_service_modifiers: None | OptionalServiceModifiers = field(
        default=None,
        metadata={
            "name": "OptionalServiceModifiers",
            "type": "Element",
        },
    )
    merchandising_availability_details: (
        None | MerchandisingAvailabilityDetails
    ) = field(
        default=None,
        metadata={
            "name": "MerchandisingAvailabilityDetails",
            "type": "Element",
        },
    )
