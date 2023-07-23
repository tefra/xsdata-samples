from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_profile_link_relationship_1 import TypeProfileLinkRelationship1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class ProfileLinkDelete1:
    """
    Delete the link between this profile and the specificied profile.

    Parameters
    ----------
    traveler_id
        The ID of the profile to link to.
    relationship
        The relationship of the link (e.g. Sibling, Spouse, etc.)
    """
    class Meta:
        name = "ProfileLinkDelete"
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
