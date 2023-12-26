from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.phone_1 import Phone1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class AgencyBaseInfo1:
    """
    Information relating to Agency.

    Parameters
    ----------
    phone
        Agency Phone Number
    """

    class Meta:
        name = "AgencyBaseInfo"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    phone: list[Phone1] = field(
        default_factory=list,
        metadata={
            "name": "Phone",
            "type": "Element",
        },
    )
