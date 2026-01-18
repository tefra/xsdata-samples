from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class StateProvType:
    """
    State, province, or region name or code needed to identify location.

    Attributes:
        value:
        state_code: The postal service standard code or abbreviation for
            the state, province, or region.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 0,
            "max_length": 64,
        },
    )
    state_code: None | str = field(
        default=None,
        metadata={
            "name": "StateCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 8,
        },
    )
