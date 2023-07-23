from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.phone_number_3 import PhoneNumber3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class AgencyContactInfo2:
    """Generic agency contact information container.

    It must contain  at least one phone number to be used by an agency
    """
    class Meta:
        name = "AgencyContactInfo"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    phone_number: list[PhoneNumber3] = field(
        default_factory=list,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
