from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_profile_link_relationship_1 import TypeProfileLinkRelationship1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class ProfileLink1:
    """
    A one way relationship between this profile and another.

    Parameters
    ----------
    traveler_id
        The ID of the profile to link to.
    relationship
        The relationship of the link (e.g. Sibling, Spouse, etc.)
    given_name
        The linked traveler's given name.  No entry required. Common
        attribute data is taken from TravelerInfo and will be returned in
        the Create, Retrieve and Modify response. This is only used in the
        response.
    other_name
        The linked traveler's other name.  No entry required. Common
        attribute data is taken from TravelerInfo and will be returned in
        the Create, Retrieve and Modify response. This is only used in the
        response.
    surname
        The linked traveler's surname.  No entry required. Common attribute
        data is taken from TravelerInfo and will be returned in the Create,
        Retrieve and Modify response. This is only used in the response.
    nickname
        The linked traveler's nickname.  No entry required. Common attribute
        data is taken from TravelerInfo and will be returned in the Create,
        Retrieve and Modify response. This is only used in the response.
    electronic_address
        The linked traveler's email.  No entry required. Common attribute
        data is taken from TravelerInfo and will be returned in the Create,
        Retrieve and Modify response. This is only used in the response.
    """
    class Meta:
        name = "ProfileLink"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    traveler_id: None | int = field(
        default=None,
        metadata={
            "name": "TravelerID",
            "type": "Attribute",
            "required": True,
        }
    )
    relationship: None | TypeProfileLinkRelationship1 = field(
        default=None,
        metadata={
            "name": "Relationship",
            "type": "Attribute",
            "required": True,
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
    other_name: None | str = field(
        default=None,
        metadata={
            "name": "OtherName",
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
    nickname: None | str = field(
        default=None,
        metadata={
            "name": "Nickname",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    electronic_address: None | str = field(
        default=None,
        metadata={
            "name": "ElectronicAddress",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
