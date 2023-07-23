from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.address_2 import Address2
from travelport.models.phone_2 import Phone2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class BranchBaseInfo2:
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
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    address: list[Address2] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    phone: list[Phone2] = field(
        default_factory=list,
        metadata={
            "name": "Phone",
            "type": "Element",
            "max_occurs": 999,
        }
    )
