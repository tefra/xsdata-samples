from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.phone_number_5 import PhoneNumber5
from travelport.models.type_structured_address_5 import TypeStructuredAddress5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class AccountInformation4:
    """
    Account Information required for File Finishing.
    """

    class Meta:
        name = "AccountInformation"
        namespace = "http://www.travelport.com/schema/common_v37_0"

    address: None | TypeStructuredAddress5 = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
        },
    )
    phone_number: list[PhoneNumber5] = field(
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
