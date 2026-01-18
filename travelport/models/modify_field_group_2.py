from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.modify_field_2 import ModifyField2
from travelport.models.type_update_action_2 import TypeUpdateAction2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class ModifyFieldGroup2:
    """
    Details of the field group and its child fields.

    To remove data from an optional attribute, omit the attribute.

    Parameters
    ----------
    modify_field
        Details of the child-level field to add, update, or remove from
        group. To remove data from an optional attribute, omit the
        attribute.
    id
        Unique identifier of the field group.
    name
        Name of the field group.
    description
        Description of the field group as a whole.
    protected
        If true, then special authorization is required for a user to create
        or modify this field or group.
    inheritable
        Denotes that the custom field group is inherited in child profiles.
        Defaults to false.
    min_occurs
        Minimum number of instances permitted (e.g., 0, 1).
    max_occurs
        Maximum number of instances permitted. Leave blank to indicate
        unlimited (i.e., ..*).
    action
        To specify whether this is an  update or delete.
    force
        To specify whether this is a Force Update or Force Delete.
    """

    class Meta:
        name = "ModifyFieldGroup"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    modify_field: list[ModifyField2] = field(
        default_factory=list,
        metadata={
            "name": "ModifyField",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    id: str = field(
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
    protected: bool = field(
        default=False,
        metadata={
            "name": "Protected",
            "type": "Attribute",
        },
    )
    inheritable: bool = field(
        default=False,
        metadata={
            "name": "Inheritable",
            "type": "Attribute",
        },
    )
    min_occurs: None | int = field(
        default=None,
        metadata={
            "name": "MinOccurs",
            "type": "Attribute",
        },
    )
    max_occurs: None | int = field(
        default=None,
        metadata={
            "name": "MaxOccurs",
            "type": "Attribute",
        },
    )
    action: TypeUpdateAction2 = field(
        metadata={
            "name": "Action",
            "type": "Attribute",
            "required": True,
        }
    )
    force: bool = field(
        default=False,
        metadata={
            "name": "Force",
            "type": "Attribute",
        },
    )
