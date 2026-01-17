from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.phone_number_1 import PhoneNumber1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class AgencyContactInfo1:
    """
    Generic agency contact information container.

    It must contain at least one phone number to be used by an agency.
    """

    class Meta:
        name = "AgencyContactInfo"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    phone_number: list[PhoneNumber1] = field(
        default_factory=list,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
