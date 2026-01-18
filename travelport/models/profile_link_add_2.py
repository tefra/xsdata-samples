from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_profile_link_relationship_2 import (
    TypeProfileLinkRelationship2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class ProfileLinkAdd2:
    """
    Add a new link between this profile and the specific profile.

    Parameters
    ----------
    traveler_id
        The ID of the profile to link to.
    relationship
        The relationship of the link (e.g. Sibling, Spouse, etc.)
    """

    class Meta:
        name = "ProfileLinkAdd"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    traveler_id: int = field(
        metadata={
            "name": "TravelerID",
            "type": "Attribute",
            "required": True,
        }
    )
    relationship: TypeProfileLinkRelationship2 = field(
        metadata={
            "name": "Relationship",
            "type": "Attribute",
            "required": True,
        }
    )
