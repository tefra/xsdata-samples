from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass(kw_only=True)
class Restriction7:
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
        namespace = "http://www.travelport.com/schema/common_v38_0"

    operation: str = field(
        metadata={
            "name": "Operation",
            "type": "Attribute",
            "required": True,
        }
    )
    reason: None | str = field(
        default=None,
        metadata={
            "name": "Reason",
            "type": "Attribute",
        },
    )
