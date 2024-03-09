from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_field_data_history_2 import TypeFieldDataHistory2
from travelport.models.type_key_element_2 import TypeKeyElement2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TypeFieldGroupDataHistory2(TypeKeyElement2):
    """
    History Element for Field Group Data.

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
        name = "typeFieldGroupDataHistory"

    field_data: list[TypeFieldDataHistory2] = field(
        default_factory=list,
        metadata={
            "name": "FieldData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            "max_occurs": 999,
        },
    )
    field_group_id: None | str = field(
        default=None,
        metadata={
            "name": "FieldGroupID",
            "type": "Attribute",
        },
    )
    owner_id: None | int = field(
        default=None,
        metadata={
            "name": "OwnerID",
            "type": "Attribute",
        },
    )
