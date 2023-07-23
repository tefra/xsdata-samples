from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.phone_number_1 import PhoneNumber1
from travelport.models.type_structured_address_1 import TypeStructuredAddress1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class AccountInformation1:
    """
    Account Information required for File Finishing.
    """
    class Meta:
        name = "AccountInformation"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    address: None | TypeStructuredAddress1 = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
        }
    )
    phone_number: list[PhoneNumber1] = field(
        default_factory=list,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    account_name: None | str = field(
        default=None,
        metadata={
            "name": "AccountName",
            "type": "Attribute",
        }
    )
