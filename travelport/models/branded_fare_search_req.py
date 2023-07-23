from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_1 import BaseReq1
from travelport.models.branded_fare_search_modifier import BrandedFareSearchModifier
from travelport.models.fare_family_criteria import FareFamilyCriteria

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class BrandedFareSearchReq(BaseReq1):
    """
    Branded Fare search request.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    fare_family_criteria: None | FareFamilyCriteria = field(
        default=None,
        metadata={
            "name": "FareFamilyCriteria",
            "type": "Element",
            "required": True,
        }
    )
    branded_fare_search_modifier: None | BrandedFareSearchModifier = field(
        default=None,
        metadata={
            "name": "BrandedFareSearchModifier",
            "type": "Element",
            "required": True,
        }
    )
