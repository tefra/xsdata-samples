from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.address_1 import Address1
from travelport.models.electronic_address_1 import ElectronicAddress1
from travelport.models.external_identifier_1 import ExternalIdentifier1
from travelport.models.phone_1 import Phone1
from travelport.models.type_account_type_profile_info_1 import (
    TypeAccountTypeProfileInfo1,
)

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class AccountInfo1(TypeAccountTypeProfileInfo1):
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
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    address: list[Address1] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
        },
    )
    phone: list[Phone1] = field(
        default_factory=list,
        metadata={
            "name": "Phone",
            "type": "Element",
        },
    )
    electronic_address: list[ElectronicAddress1] = field(
        default_factory=list,
        metadata={
            "name": "ElectronicAddress",
            "type": "Element",
        },
    )
    external_identifier: list[ExternalIdentifier1] = field(
        default_factory=list,
        metadata={
            "name": "ExternalIdentifier",
            "type": "Element",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        },
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
