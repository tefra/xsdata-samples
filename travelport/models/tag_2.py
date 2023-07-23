from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class Tag2:
    """
    A tag that belongs to the agency.

    Parameters
    ----------
    name
        The name given to the tag
    label
        The alternate name given to the tag
    description
        The description of the tag
    display_order
        The display order of the tag
    id
        The unique identifier of the tag.
    agency_id
        The agency that owns the tag
    """
    class Meta:
        name = "Tag"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    label: None | str = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Attribute",
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
        }
    )
    display_order: None | int = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        }
    )
    agency_id: None | int = field(
        default=None,
        metadata={
            "name": "AgencyID",
            "type": "Attribute",
            "required": True,
        }
    )
