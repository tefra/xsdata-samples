from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_taggable_phone_2 import TypeTaggablePhone2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class AlternateContactPhone2(TypeTaggablePhone2):
    """
    Alternate contact phone.

    Parameters
    ----------
    alternate_contact_ref
        Key referencing to alternate contact.
    """

    class Meta:
        name = "AlternateContactPhone"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    alternate_contact_ref: None | str = field(
        default=None,
        metadata={
            "name": "AlternateContactRef",
            "type": "Attribute",
            "required": True,
        },
    )
