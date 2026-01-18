from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.address_1 import Address1
from travelport.models.phone_1 import Phone1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass(kw_only=True)
class BranchBaseInfo1:
    """
    Information relating to Branch.

    Parameters
    ----------
    address
        Branch Address
    phone
        Branch Phone Number
    """

    class Meta:
        name = "BranchBaseInfo"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    address: list[Address1] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
        },
    )
    phone: list[Phone1] = field(
        default_factory=list,
        metadata={
            "name": "Phone",
            "type": "Element",
        },
    )
