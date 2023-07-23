from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_profile_data_element_type_1 import TypeProfileDataElementType1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class ProfileDataDelete1:
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
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    element: None | TypeProfileDataElementType1 = field(
        default=None,
        metadata={
            "name": "Element",
            "type": "Attribute",
            "required": True,
        }
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
