from __future__ import annotations

from dataclasses import dataclass

from travelport.models.base_air_price_rsp import BaseAirPriceRsp

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class AirPriceRsp(BaseAirPriceRsp):
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"
