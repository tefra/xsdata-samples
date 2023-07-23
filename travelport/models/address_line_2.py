from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class AddressLine2:
    """
    Specifies a single line within an address.
    """
    class Meta:
        name = "AddressLine"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
