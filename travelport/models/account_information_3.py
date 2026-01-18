from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.phone_number_4 import PhoneNumber4
from travelport.models.type_structured_address_4 import TypeStructuredAddress4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass(kw_only=True)
class AccountInformation3:
    """
    Account Information required for File Finishing.
    """

    class Meta:
        name = "AccountInformation"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    address: None | TypeStructuredAddress4 = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
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
    account_name: None | str = field(
        default=None,
        metadata={
            "name": "AccountName",
            "type": "Attribute",
        },
    )
