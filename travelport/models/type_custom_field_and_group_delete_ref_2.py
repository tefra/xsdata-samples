from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TypeCustomFieldAndGroupDeleteRef2:
    """
    A reference to an endpoint.

    Parameters
    ----------
    id
        Unique identifier of the Custom Field or Group.
    """

    class Meta:
        name = "typeCustomFieldAndGroupDeleteRef"

    id: None | str = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        },
    )
