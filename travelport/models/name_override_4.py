from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class NameOverride4:
    """
    To be used if the name is different from booking travelers in the PNR.

    Parameters
    ----------
    first
        First Name.
    last
        Last Name.
    """

    class Meta:
        name = "NameOverride"
        namespace = "http://www.travelport.com/schema/common_v37_0"

    first: None | str = field(
        default=None,
        metadata={
            "name": "First",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    last: None | str = field(
        default=None,
        metadata={
            "name": "Last",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
