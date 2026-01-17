from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_taggable_element_1 import TypeTaggableElement1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class TagAdd1:
    """
    Add a tag to the specified element of the profile.

    There are two methods to add tag to profile data - One is through this
    TagAdd element and another is through TagRef element.

    Parameters
    ----------
    element
        The type of element to add the tag to.
    key
        The unique identifier of the specific element into which the tag
        will be added.
    tag_id
        The ID of the tag to add.
    """

    class Meta:
        name = "TagAdd"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    element: None | TypeTaggableElement1 = field(
        default=None,
        metadata={
            "name": "Element",
            "type": "Attribute",
            "required": True,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        },
    )
    tag_id: None | str = field(
        default=None,
        metadata={
            "name": "TagID",
            "type": "Attribute",
            "required": True,
        },
    )
