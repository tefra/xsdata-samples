from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_element_status_1 import TypeElementStatus1

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass
class RailFareNote:
    """A simple textual fare note.

    Used within several other objects.

    Parameters
    ----------
    value
    key
    note_name
    el_stat
        This attribute is used to show the action results of an element.
        Possible values are "A" (when elements have been added to the UR)
        and "M" (when existing elements have been modified). Response only.
    key_override
        If a duplicate key is found where we are adding elements in some
        cases like URAdd, then instead of erroring out set this attribute to
        true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    value: str = field(
        default="",
        metadata={
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
    note_name: None | str = field(
        default=None,
        metadata={
            "name": "NoteName",
            "type": "Attribute",
            "required": True,
        }
    )
    el_stat: None | TypeElementStatus1 = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: None | bool = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )
