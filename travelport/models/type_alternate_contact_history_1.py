from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_contact_type_1 import TypeContactType1
from travelport.models.type_key_element_1 import TypeKeyElement1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class TypeAlternateContactHistory1(TypeKeyElement1):
    """
    History Element for Contact info.

    Parameters
    ----------
    type_value
        A code for categorizing contactees based on a role they might play.
        Examples include Emergency Contact, Regular Contact, Backup Contact,
        etc.
    given_name
        The given name(s) of a person.  May also be known as First Name in
        some cultures.
    surname
        Surname(s) or family names for a person.  May be known as Last Names
        in some cultures.
    other_name
        Name(s) for a person other than given or surnames.  Includes those
        known as Middle Names in some cultures, but may include other names
        such as maiden names.
    nickname
        A alternative name for a person that maybe used informally or at the
        preference of a person.  Examples include diminutive versions of
        names ("Katie" instead of "Katherine"), shortened versions of longer
        names,  or common substitution names ("Jack" instead of "John").
    priority_order
        Priority order associated with this Contact.
    """
    class Meta:
        name = "typeAlternateContactHistory"

    type_value: None | TypeContactType1 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    given_name: None | str = field(
        default=None,
        metadata={
            "name": "GivenName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    surname: None | str = field(
        default=None,
        metadata={
            "name": "Surname",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    other_name: None | str = field(
        default=None,
        metadata={
            "name": "OtherName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    nickname: None | str = field(
        default=None,
        metadata={
            "name": "Nickname",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    priority_order: None | int = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )
