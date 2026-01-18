from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_geo_political_area_filter_type_2 import (
    TypeGeoPoliticalAreaFilterType2,
)
from travelport.models.type_geo_political_area_type_2 import (
    TypeGeoPoliticalAreaType2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class GeoPoliticalAreaFilter2:
    """
    Retrieve part or parts of profile by a particular geographic location
    for the specified data category.Geographical location is only
    applicable to the following categories:- All Preferences, Air
    Preference, Vehicle Preference, Hotel Preference, Rail Preference and
    Other Preference.
    """

    class Meta:
        name = "GeoPoliticalAreaFilter"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    filter_type: TypeGeoPoliticalAreaFilterType2 = field(
        metadata={
            "name": "FilterType",
            "type": "Attribute",
            "required": True,
        }
    )
    geo_political_area_type: TypeGeoPoliticalAreaType2 = field(
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
