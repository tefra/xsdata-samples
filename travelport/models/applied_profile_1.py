from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_element_status_1 import TypeElementStatus1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class AppliedProfile1:
    """
    A simple container to specify the profiles that were applied to a reservation.

    Parameters
    ----------
    key
        Key for update/delete of the element
    traveler_id
        The ID of the TravelerProfile that was applied
    traveler_name
        The name from the TravelerProfile that was applied
    account_id
        The ID of the AccountProfile that was applied
    account_name
        The name from the AccountProfile that was applied
    immediate_parent_id
        The ID of the immediate parent that was applied
    immediate_parent_name
        The name of the immediate parent that was applied
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
        name = "AppliedProfile"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    traveler_id: None | str = field(
        default=None,
        metadata={
            "name": "TravelerID",
            "type": "Attribute",
        },
    )
    traveler_name: None | str = field(
        default=None,
        metadata={
            "name": "TravelerName",
            "type": "Attribute",
        },
    )
    account_id: None | str = field(
        default=None,
        metadata={
            "name": "AccountID",
            "type": "Attribute",
        },
    )
    account_name: None | str = field(
        default=None,
        metadata={
            "name": "AccountName",
            "type": "Attribute",
        },
    )
    immediate_parent_id: None | str = field(
        default=None,
        metadata={
            "name": "ImmediateParentID",
            "type": "Attribute",
        },
    )
    immediate_parent_name: None | str = field(
        default=None,
        metadata={
            "name": "ImmediateParentName",
            "type": "Attribute",
        },
    )
    el_stat: None | TypeElementStatus1 = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        },
    )
    key_override: None | bool = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        },
    )
