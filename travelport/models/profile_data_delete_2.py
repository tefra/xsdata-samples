from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_profile_data_element_type_2 import (
    TypeProfileDataElementType2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class ProfileDataDelete2:
    """
    Delete one element of given type identified by its key.

    Parameters
    ----------
    element
        The type of element in the profile.
    key
        The identifier of the element that will be delete from this profile.
    """

    class Meta:
        name = "ProfileDataDelete"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    element: TypeProfileDataElementType2 = field(
        metadata={
            "name": "Element",
            "type": "Attribute",
            "required": True,
        }
    )
    key: str = field(
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
