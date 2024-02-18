from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.geo_political_area_filter_2 import (
    GeoPoliticalAreaFilter2,
)
from travelport.models.profile_data_category_2 import ProfileDataCategory2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileDataFilter2:
    """Filters the data in the profile so that only the specified data is returned.

    Multiple categories can be applied if more data is needed on the
    response.  If no filter is specified then "General Information" is
    defaulted.  If duplicate categories are specifed they are ignored.
    """

    class Meta:
        name = "ProfileDataFilter"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_data_category: list[ProfileDataCategory2] = field(
        default_factory=list,
        metadata={
            "name": "ProfileDataCategory",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    geo_political_area_filter: list[GeoPoliticalAreaFilter2] = field(
        default_factory=list,
        metadata={
            "name": "GeoPoliticalAreaFilter",
            "type": "Element",
            "max_occurs": 999,
        },
    )
