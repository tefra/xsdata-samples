from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_profile_link_relationship_1 import (
    TypeProfileLinkRelationship1,
)

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class TypeProfileLinkHistory1:
    """
    History Element for ProfileLink Add.

    Parameters
    ----------
    traveler_id
        The ID of the profile to link to.
    relationship
        The relationship of the link (e.g. Sibling, Spouse, etc.)
    given_name
        The linked traveler's given name.  Will be returned on profile
        response.
    other_name
        The linked traveler's other name.  Will be returned on profile
        response.
    surname
        The linked traveler's surname.  Will be returned on profile
        response.
    nickname
        The linked traveler's nickname.  Will be returned on profile
        response.
    electronic_address
        The linked traveler's email.  Will be returned on profile response.
    """

    class Meta:
        name = "typeProfileLinkHistory"

    traveler_id: None | int = field(
        default=None,
        metadata={
            "name": "TravelerID",
            "type": "Attribute",
        },
    )
    relationship: None | TypeProfileLinkRelationship1 = field(
        default=None,
        metadata={
            "name": "Relationship",
            "type": "Attribute",
        },
    )
    given_name: None | str = field(
        default=None,
        metadata={
            "name": "GivenName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    other_name: None | str = field(
        default=None,
        metadata={
            "name": "OtherName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    surname: None | str = field(
        default=None,
        metadata={
            "name": "Surname",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    nickname: None | str = field(
        default=None,
        metadata={
            "name": "Nickname",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    electronic_address: None | str = field(
        default=None,
        metadata={
            "name": "ElectronicAddress",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
