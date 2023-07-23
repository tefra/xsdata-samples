from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_search_rsp import AirSearchRsp
from travelport.models.brand_list import BrandList

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class LowFareSearchRsp(AirSearchRsp):
    """
    Low Fare Search Response.

    Parameters
    ----------
    brand_list
    currency_type
        Provider: 1G,1V,1P,ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    brand_list: None | BrandList = field(
        default=None,
        metadata={
            "name": "BrandList",
            "type": "Element",
        }
    )
    currency_type: None | str = field(
        default=None,
        metadata={
            "name": "CurrencyType",
            "type": "Attribute",
            "required": True,
            "length": 3,
        }
    )
