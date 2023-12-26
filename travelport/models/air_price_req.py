from __future__ import annotations
from dataclasses import dataclass
from travelport.models.base_air_price_req import BaseAirPriceReq

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirPriceReq(BaseAirPriceReq):
    """Request to price an itinerary in one to many ways.

    Pricing commands can be specified globally, or specifically per
    command.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"
