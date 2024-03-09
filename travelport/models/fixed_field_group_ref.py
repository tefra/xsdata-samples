from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class FixedFieldGroupRef:
    """
    Unique ID of a field group that this field can reference values from (by their
    Key) at the time of creating or modifying profiles.

    Parameters
    ----------
    id
        The unique ID of the reference-able fixed field group.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    id: None | str = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        },
    )
