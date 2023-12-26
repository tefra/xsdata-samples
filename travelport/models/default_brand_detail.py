from __future__ import annotations
from dataclasses import dataclass
from travelport.models.type_default_brand_detail import TypeDefaultBrandDetail

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class DefaultBrandDetail(TypeDefaultBrandDetail):
    """
    Applicable air segment.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"
