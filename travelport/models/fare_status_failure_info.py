from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class FareStatusFailureInfo:
    """
    Denotes the failure reason of a particular fare.

    Parameters
    ----------
    code
        The failure code of the fare.
    reason
        The reason for the failure.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    code: str = field(
        metadata={
            "name": "Code",
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
