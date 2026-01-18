from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.geo_political_area_filter_1 import (
    GeoPoliticalAreaFilter1,
)
from travelport.models.profile_data_category_1 import ProfileDataCategory1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass(kw_only=True)
class ProfileDataFilter1:
    """
    Filters the data in the profile so that only the specified data is
    returned.

    Multiple categories can be applied if more data is needed on the
    response. If no filter is specified then "General Information" is
    defaulted. If duplicate categories are specifed they are ignored.
    """

    class Meta:
        name = "ProfileDataFilter"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    profile_data_category: list[ProfileDataCategory1] = field(
        default_factory=list,
        metadata={
            "name": "ProfileDataCategory",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    geo_political_area_filter: list[GeoPoliticalAreaFilter1] = field(
        default_factory=list,
        metadata={
            "name": "GeoPoliticalAreaFilter",
            "type": "Element",
        },
    )
