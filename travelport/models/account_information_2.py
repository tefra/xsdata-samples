from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.phone_number_3 import PhoneNumber3
from travelport.models.type_structured_address_3 import TypeStructuredAddress3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass(kw_only=True)
class AccountInformation2:
    """
    Account Information required for File Finishing.
    """

    class Meta:
        name = "AccountInformation"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    address: None | TypeStructuredAddress3 = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
        },
    )
    phone_number: list[PhoneNumber3] = field(
        default_factory=list,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    account_name: None | str = field(
        default=None,
        metadata={
            "name": "AccountName",
            "type": "Attribute",
        },
    )
