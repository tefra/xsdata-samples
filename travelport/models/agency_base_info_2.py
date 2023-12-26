from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.phone_2 import Phone2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class AgencyBaseInfo2:
    """
    Information relating to Agency.

    Parameters
    ----------
    phone
        Agency Phone Number
    """

    class Meta:
        name = "AgencyBaseInfo"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    phone: list[Phone2] = field(
        default_factory=list,
        metadata={
            "name": "Phone",
            "type": "Element",
            "max_occurs": 999,
        },
    )
