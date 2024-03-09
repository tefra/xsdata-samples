from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.phone_number_7 import PhoneNumber7
from travelport.models.type_structured_address_7 import TypeStructuredAddress7

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class AccountInformation6:
    """
    Account Information required for File Finishing.
    """

    class Meta:
        name = "AccountInformation"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    address: None | TypeStructuredAddress7 = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
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
    account_name: None | str = field(
        default=None,
        metadata={
            "name": "AccountName",
            "type": "Attribute",
        },
    )
