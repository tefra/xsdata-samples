from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.phone_number_6 import PhoneNumber6
from travelport.models.type_structured_address_6 import TypeStructuredAddress6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass(kw_only=True)
class AccountInformation5:
    """
    Account Information required for File Finishing.
    """

    class Meta:
        name = "AccountInformation"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    address: None | TypeStructuredAddress6 = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
        },
    )
    phone_number: list[PhoneNumber6] = field(
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
