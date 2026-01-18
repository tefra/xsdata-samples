from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_custom_field_1 import TypeCustomField1
from travelport.models.type_profile_type_3 import TypeProfileType3

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass(kw_only=True)
class Field1(TypeCustomField1):
    """
    Specify any existing fields that belong to this group.

    Parameters
    ----------
    profile_id
        The profile ID of the agency or account that the field belongs to.
    profile_type
        The type of the Profile to be created.
    is_used
        True if the custom field is in use by one or more profiles.
    """

    class Meta:
        name = "Field"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    profile_id: int = field(
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_type: TypeProfileType3 = field(
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        }
    )
    is_used: bool = field(
        metadata={
            "name": "IsUsed",
            "type": "Attribute",
            "required": True,
        }
    )
