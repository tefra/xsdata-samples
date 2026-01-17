from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_profile_data_category_1 import (
    TypeProfileDataCategory1,
)

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class ProfileDataCategory1:
    """
    The category of data that controls what data will be returned in the
    response.
    """

    class Meta:
        name = "ProfileDataCategory"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    value: None | TypeProfileDataCategory1 = field(
        default=None,
        metadata={
            "required": True,
        },
    )
