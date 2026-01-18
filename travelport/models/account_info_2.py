from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.address_2 import Address2
from travelport.models.electronic_address_2 import ElectronicAddress2
from travelport.models.external_identifier_2 import ExternalIdentifier2
from travelport.models.phone_2 import Phone2
from travelport.models.type_account_type_profile_info_2 import (
    TypeAccountTypeProfileInfo2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class AccountInfo2(TypeAccountTypeProfileInfo2):
    """
    Account specific profile information.

    Parameters
    ----------
    address
        Account Address
    phone
        Account Phone Number
    electronic_address
        Account Electronic Address
    external_identifier
        Account External Identifier
    name
        The name of the account.
    local_language_name
        The name of the account in the user's local language.
    """

    class Meta:
        name = "AccountInfo"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    address: list[Address2] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    phone: list[Phone2] = field(
        default_factory=list,
        metadata={
            "name": "Phone",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    electronic_address: list[ElectronicAddress2] = field(
        default_factory=list,
        metadata={
            "name": "ElectronicAddress",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    external_identifier: list[ExternalIdentifier2] = field(
        default_factory=list,
        metadata={
            "name": "ExternalIdentifier",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    name: str = field(
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    local_language_name: None | str = field(
        default=None,
        metadata={
            "name": "LocalLanguageName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
