from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ModifyTag2:
    """
    Parameters
    ----------
    id
        The ID of the tag to be modified.
    name
        The name given to the tag.  If not specified, then not changed.
    label
        The alternate name given to the tag.  If not specified, then not
        changed.
    description
        The description of the tag.  If not specified, then not changed.
    display_order
        The display order of the tag
    """
    class Meta:
        name = "ModifyTag"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    id: None | str = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        }
    )
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 50,
        }
    )
    label: None | str = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 50,
        }
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    display_order: None | int = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        }
    )
