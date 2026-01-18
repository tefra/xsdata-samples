from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass(kw_only=True)
class RailSupplier:
    """
    Parameters
    ----------
    code
        2 character Rail distributor code.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    code: str = field(
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        }
    )
