from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_common_editable_group_2 import (
    TypeCommonEditableGroup2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class FixedGroupUpdate(TypeCommonEditableGroup2):
    """Update the agency-defined attributes for a fixed field group.

    To remove a value, omit the attribute entirely.

    Parameters
    ----------
    max_occurs
        Maximum number of instances permitted.
    min_occurs
        Minimum number of instances permitted (e.g., 0, 1).  Leave blank to
        indicate 0.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    max_occurs: None | int = field(
        default=None,
        metadata={
            "name": "MaxOccurs",
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
