from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.email_6 import Email6
from travelport.models.phone_number_7 import PhoneNumber7
from travelport.models.type_structured_address_7 import TypeStructuredAddress7

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass(kw_only=True)
class AgencyInformation6:
    """
    Agency Information required for File Finishing.
    """

    class Meta:
        name = "AgencyInformation"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    address: None | TypeStructuredAddress7 = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
        },
    )
    email: list[Email6] = field(
        default_factory=list,
        metadata={
            "name": "Email",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    phone_number: list[PhoneNumber7] = field(
        default_factory=list,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "max_occurs": 999,
        },
    )
