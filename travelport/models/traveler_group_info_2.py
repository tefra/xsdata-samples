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


@dataclass
class TravelerGroupInfo2(TypeAccountTypeProfileInfo2):
    """
    Traveler group specific profile information.

    Parameters
    ----------
    address
        Traveler Group Address
    phone
        Traveler Group Phone Number
    electronic_address
        Traveler Group Electronic Address
    external_identifier
        Traveler Group External Identifier
    name
        Name of the TravelerGroup
    local_language_name
        The name of the TravelerGroup in the user's local language.
    """

    class Meta:
        name = "TravelerGroupInfo"
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
