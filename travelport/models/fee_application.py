from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class FeeApplication:
    """
    Parameters
    ----------
    value
    code
        The code associated to the fee application. The  choices are: 1, 2,
        3, 4, 5, K, F
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    code: None | str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "length": 1,
        },
    )
