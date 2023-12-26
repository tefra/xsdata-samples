from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_profile_link_relationship_2 import (
    TypeProfileLinkRelationship2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileLinkDelete2:
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
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    traveler_id: None | int = field(
        default=None,
        metadata={
            "name": "TravelerID",
            "type": "Attribute",
            "required": True,
        },
    )
    relationship: None | TypeProfileLinkRelationship2 = field(
        default=None,
        metadata={
            "name": "Relationship",
            "type": "Attribute",
            "required": True,
        },
    )
