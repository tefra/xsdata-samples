from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.tag_ref_2 import TagRef2
from travelport.models.type_contact_purpose_2 import TypeContactPurpose2
from travelport.models.type_phone_2 import TypePhone2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class TypeTaggablePhone2(TypePhone2):
    """
    Base type of a phone that is taggable.

    Parameters
    ----------
    tag_ref
    purpose
        A code for categorizing a contact mechanism based on purpose or use.
        Examples include business, persona., etc.
    priority_order
        Priority order associated with this Phone.
    """

    class Meta:
        name = "typeTaggablePhone"

    tag_ref: list[TagRef2] = field(
        default_factory=list,
        metadata={
            "name": "TagRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            "max_occurs": 999,
        },
    )
    purpose: None | TypeContactPurpose2 = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Attribute",
        },
    )
    priority_order: None | int = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        },
    )
