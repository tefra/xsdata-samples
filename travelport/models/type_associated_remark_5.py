from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_element_status_6 import TypeElementStatus6
from travelport.models.type_remark_with_traveler_ref_5 import (
    TypeRemarkWithTravelerRef5,
)

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class TypeAssociatedRemark5(TypeRemarkWithTravelerRef5):
    """
    A textual remark container to hold Associated itinerary remarks.

    Parameters
    ----------
    key
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
        name = "typeAssociatedRemark"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    el_stat: None | TypeElementStatus6 = field(
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
