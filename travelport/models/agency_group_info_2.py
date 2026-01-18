from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.address_2 import Address2
from travelport.models.electronic_address_2 import ElectronicAddress2
from travelport.models.external_identifier_2 import ExternalIdentifier2
from travelport.models.phone_2 import Phone2
from travelport.models.type_profile_info_2 import TypeProfileInfo2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class AgencyGroupInfo2(TypeProfileInfo2):
    """
    Information relating to Agency Group.

    Parameters
    ----------
    address
        Agency Group Address
    phone
        Agency Group Phone Number
    electronic_address
        Agency Group Electronic Address
    external_identifier
        Agency Group External Identifier
    name
        Name of Agency Group
    """

    class Meta:
        name = "AgencyGroupInfo"
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
