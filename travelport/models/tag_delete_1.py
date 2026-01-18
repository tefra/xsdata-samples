from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_taggable_element_1 import TypeTaggableElement1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass(kw_only=True)
class TagDelete1:
    """
    Delete a tag from the specified element of the profile.

    There are two methods to delete tag from profile data - One is through
    this TagDelete element and another is through TagRef. To delete the
    last Tag associated to a ProfileData use TagDelete element.

    Parameters
    ----------
    element
        The type of element to remove the tag from.
    key
        The unique identifier of the specific element from which the tag
        will be deleted.
    tag_id
        The ID of the tag to delete.
    """

    class Meta:
        name = "TagDelete"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    element: TypeTaggableElement1 = field(
        metadata={
            "name": "Element",
            "type": "Attribute",
            "required": True,
        }
    )
    key: str = field(
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    tag_id: str = field(
        metadata={
            "name": "TagID",
            "type": "Attribute",
            "required": True,
        }
    )
