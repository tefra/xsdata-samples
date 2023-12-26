from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_contact_type_2 import TypeContactType2
from travelport.models.type_search_address_2 import TypeSearchAddress2
from travelport.models.type_search_electronic_address_2 import (
    TypeSearchElectronicAddress2,
)
from travelport.models.type_search_phone_2 import TypeSearchPhone2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TypeSearchContact2:
    """
    Defines the Contact attributes allowed in searching.

    Parameters
    ----------
    given_name
    other_name
    surname
    nick_name
    address
    phone
    electronic_address
    type_value
        A code for categorizing contactees based on a role they might play.
        Examples include Emergency Contact, Regular Contact, Backup Contact,
        etc.
    """

    class Meta:
        name = "typeSearchContact"

    given_name: None | str = field(
        default=None,
        metadata={
            "name": "GivenName",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    other_name: None | str = field(
        default=None,
        metadata={
            "name": "OtherName",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    surname: None | str = field(
        default=None,
        metadata={
            "name": "Surname",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    nick_name: None | str = field(
        default=None,
        metadata={
            "name": "NickName",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    address: None | TypeSearchAddress2 = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    phone: None | TypeSearchPhone2 = field(
        default=None,
        metadata={
            "name": "Phone",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    electronic_address: None | TypeSearchElectronicAddress2 = field(
        default=None,
        metadata={
            "name": "ElectronicAddress",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    type_value: None | TypeContactType2 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
