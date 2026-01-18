from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.email_3 import Email3
from travelport.models.phone_number_4 import PhoneNumber4
from travelport.models.type_structured_address_4 import TypeStructuredAddress4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass(kw_only=True)
class AgencyInformation3:
    """
    Agency Information required for File Finishing.
    """

    class Meta:
        name = "AgencyInformation"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    address: None | TypeStructuredAddress4 = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
        },
    )
    email: list[Email3] = field(
        default_factory=list,
        metadata={
            "name": "Email",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    phone_number: list[PhoneNumber4] = field(
        default_factory=list,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "max_occurs": 999,
        },
    )
