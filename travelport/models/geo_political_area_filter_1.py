from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_geo_political_area_filter_type_1 import (
    TypeGeoPoliticalAreaFilterType1,
)
from travelport.models.type_geo_political_area_type_1 import (
    TypeGeoPoliticalAreaType1,
)

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass(kw_only=True)
class GeoPoliticalAreaFilter1:
    """
    Retrieve part or parts of profile by a particular geographic location
    for the specified data category.Geographical location is only
    applicable to the following categories:- All Preferences, Air
    Preference, Vehicle Preference, Hotel Preference, Rail Preference and
    Other Preference.
    """

    class Meta:
        name = "GeoPoliticalAreaFilter"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    filter_type: TypeGeoPoliticalAreaFilterType1 = field(
        metadata={
            "name": "FilterType",
            "type": "Attribute",
            "required": True,
        }
    )
    geo_political_area_type: TypeGeoPoliticalAreaType1 = field(
        metadata={
            "name": "GeoPoliticalAreaType",
            "type": "Attribute",
            "required": True,
        }
    )
    geo_political_area_code: str = field(
        metadata={
            "name": "GeoPoliticalAreaCode",
            "type": "Attribute",
            "required": True,
            "max_length": 6,
        }
    )
