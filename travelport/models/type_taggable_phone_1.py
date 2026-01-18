from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.tag_ref_1 import TagRef1
from travelport.models.type_contact_purpose_1 import TypeContactPurpose1
from travelport.models.type_phone_1 import TypePhone1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass(kw_only=True)
class TypeTaggablePhone1(TypePhone1):
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

    tag_ref: list[TagRef1] = field(
        default_factory=list,
        metadata={
            "name": "TagRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    purpose: None | TypeContactPurpose1 = field(
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
