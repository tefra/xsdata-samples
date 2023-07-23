from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.field_data_1 import FieldData1
from travelport.models.type_key_tagged_element_1 import TypeKeyTaggedElement1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class FieldGroupData1(TypeKeyTaggedElement1):
    """
    Parameters
    ----------
    field_data
        Data values associated to this entity. Each value is linked to a
        field instance, which defines the attributes of the field specific
        to the associated template or its parent field group.
    field_group_id
        The unique ID of the template field group (instance of a field group
        on a template) that this value is applied to.
    owner_id
        Id of the profile who owns the Traveler's proprietary data.Should be
        the immediate parent id of the traveler.
    """
    class Meta:
        name = "FieldGroupData"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    field_data: list[FieldData1] = field(
        default_factory=list,
        metadata={
            "name": "FieldData",
            "type": "Element",
        }
    )
    field_group_id: None | str = field(
        default=None,
        metadata={
            "name": "FieldGroupID",
            "type": "Attribute",
            "required": True,
        }
    )
    owner_id: None | int = field(
        default=None,
        metadata={
            "name": "OwnerID",
            "type": "Attribute",
        }
    )
