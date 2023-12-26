from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_2 import BaseReq2
from travelport.models.create_field_1 import CreateField1
from travelport.models.create_field_group_1 import CreateFieldGroup1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class ProfileCreateFieldReq1(BaseReq2):
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
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    create_field: list[CreateField1] = field(
        default_factory=list,
        metadata={
            "name": "CreateField",
            "type": "Element",
        },
    )
    create_field_group: list[CreateFieldGroup1] = field(
        default_factory=list,
        metadata={
            "name": "CreateFieldGroup",
            "type": "Element",
        },
    )
    profile_id: None | int = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
            "required": True,
        },
    )
