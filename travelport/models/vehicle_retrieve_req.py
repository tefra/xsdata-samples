from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_1 import BaseReq1

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass(kw_only=True)
class VehicleRetrieveReq(BaseReq1):
    """
    PNR Retrieve request for a vehicle booking.

    Given a provider code and a provider locator code.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    provider_code: str = field(
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )
    provider_locator_code: str = field(
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "required": True,
            "max_length": 15,
        }
    )
