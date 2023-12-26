from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_contact_type_1 import TypeContactType1
from travelport.models.type_search_address_1 import TypeSearchAddress1
from travelport.models.type_search_electronic_address_1 import (
    TypeSearchElectronicAddress1,
)
from travelport.models.type_search_phone_1 import TypeSearchPhone1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class TypeSearchContact1:
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
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    other_name: None | str = field(
        default=None,
        metadata={
            "name": "OtherName",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    surname: None | str = field(
        default=None,
        metadata={
            "name": "Surname",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    nick_name: None | str = field(
        default=None,
        metadata={
            "name": "NickName",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    address: None | TypeSearchAddress1 = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    phone: None | TypeSearchPhone1 = field(
        default=None,
        metadata={
            "name": "Phone",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    electronic_address: None | TypeSearchElectronicAddress1 = field(
        default=None,
        metadata={
            "name": "ElectronicAddress",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    type_value: None | TypeContactType1 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
