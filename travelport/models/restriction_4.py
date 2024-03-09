from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class Restriction4:
    """
    Which activities are supported for a particular element.

    Parameters
    ----------
    operation
        The operation that is restricted
    reason
        The reason it is restricted
    """

    class Meta:
        name = "Restriction"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    operation: None | str = field(
        default=None,
        metadata={
            "name": "Operation",
            "type": "Attribute",
            "required": True,
        },
    )
    reason: None | str = field(
        default=None,
        metadata={
            "name": "Reason",
            "type": "Attribute",
        },
    )
