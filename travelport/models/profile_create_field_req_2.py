from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_5 import BaseReq5
from travelport.models.create_field_2 import CreateField2
from travelport.models.create_field_group_2 import CreateFieldGroup2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileCreateFieldReq2(BaseReq5):
    """
    Creates one or multiple custom fields and/or field groups.

    Parameters
    ----------
    create_field
        Defines the attributes of a new custom field.
    create_field_group
        Defines the attributes and structure of a new custom field group,
        and the custom fields that belong to it.
    profile_id
        The ID of the agency or account profile that will own the field(s)
        and group(s) to be created.
    """
    class Meta:
        name = "ProfileCreateFieldReq"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    create_field: list[CreateField2] = field(
        default_factory=list,
        metadata={
            "name": "CreateField",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    create_field_group: list[CreateFieldGroup2] = field(
        default_factory=list,
        metadata={
            "name": "CreateFieldGroup",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    profile_id: None | int = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
            "required": True,
        }
    )
