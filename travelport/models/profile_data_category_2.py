from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_profile_data_category_2 import (
    TypeProfileDataCategory2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class ProfileDataCategory2:
    """
    The category of data that controls what data will be returned in the
    response.
    """

    class Meta:
        name = "ProfileDataCategory"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    value: TypeProfileDataCategory2 = field(
        metadata={
            "required": True,
        }
    )
