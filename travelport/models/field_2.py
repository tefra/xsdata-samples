from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_custom_field_2 import TypeCustomField2
from travelport.models.type_profile_type_7 import TypeProfileType7

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class Field2(TypeCustomField2):
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
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_id: None | int = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
            "required": True,
        }
    )
    profile_type: None | TypeProfileType7 = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        }
    )
    is_used: None | bool = field(
        default=None,
        metadata={
            "name": "IsUsed",
            "type": "Attribute",
            "required": True,
        }
    )
